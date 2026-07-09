from pathlib import Path
import json

from fastapi.testclient import TestClient

from app.main import app


def test_health_route():
    client = TestClient(app)

    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_index_route_renders():
    client = TestClient(app)

    response = client.get("/")

    assert response.status_code == 200
    assert "Phishing Email Analyzer" in response.text


def test_analyze_requires_email_input():
    client = TestClient(app)

    response = client.post("/analyze", data={"pasted_email": ""})

    assert response.status_code == 400
    assert "Paste email content or upload a .eml file before analyzing." in response.text


def test_analyze_rejects_empty_eml_sample():
    client = TestClient(app)

    sample_bytes = Path("samples/empty_error_sample.eml").read_bytes()
    response = client.post(
        "/analyze",
        files={"eml_file": ("empty_error_sample.eml", sample_bytes, "message/rfc822")},
    )

    assert response.status_code == 400
    assert "Paste email content or upload a .eml file before analyzing." in response.text


def test_analyze_rejects_invalid_file_type():
    client = TestClient(app)

    sample_bytes = Path("samples/invalid_upload.txt").read_bytes()
    response = client.post(
        "/analyze",
        files={"eml_file": ("invalid_upload.txt", sample_bytes, "text/plain")},
    )

    assert response.status_code == 400
    assert "Invalid file type. Upload a .eml email file" in response.text


def test_analyze_accepts_sample_eml_upload():
    client = TestClient(app)

    sample_bytes = Path("samples/business_invoice_medium.eml").read_bytes()
    response = client.post(
        "/analyze",
        files={"eml_file": ("business_invoice_medium.eml", sample_bytes, "message/rfc822")},
    )

    assert response.status_code == 200
    assert "Analysis completed successfully." in response.text
    assert "Medium phishing risk" in response.text


def test_analyze_renders_sample_llm_report_with_long_explanation(monkeypatch):
    client = TestClient(app)
    llm_report = json.loads(Path("samples/llm_long_response_sample.json").read_text(encoding="utf-8"))

    async def sample_analyze_email(parsed_email):
        return {
            "score": 61,
            "severity": "Medium",
            "summary": "Medium phishing risk (61/100). Review the listed indicators carefully.",
            "analysis_mode": "Heuristics + sample OpenAI response",
            "indicators": [
                {
                    "type": "Header mismatch",
                    "value": "billing-help@external-mail.example",
                    "reason": "Reply-To differs from the visible From header.",
                }
            ],
            "parsed_email": {
                "subject": parsed_email.subject,
                "from_header": parsed_email.from_header,
                "reply_to": parsed_email.reply_to,
                "return_path": parsed_email.return_path,
                "to_header": parsed_email.to_header,
                "date": parsed_email.date,
                "authentication_results": parsed_email.authentication_results,
                "received_headers": parsed_email.received_headers,
                "body_text": parsed_email.body_text,
                "urls": parsed_email.urls,
                "attachment_names": parsed_email.attachment_names,
            },
            "llm_report": llm_report,
        }

    monkeypatch.setattr("app.main.analyze_email", sample_analyze_email)

    raw_email = Path("samples/business_invoice_medium.eml").read_text(encoding="utf-8")
    response = client.post("/analyze", data={"pasted_email": raw_email})

    assert response.status_code == 200
    assert "Analyst Report" in response.text
    assert "extended LLM analyst text remains readable" in response.text
    assert "Do not open the attachment or click any links" in response.text
