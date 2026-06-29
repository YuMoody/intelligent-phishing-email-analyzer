from pathlib import Path

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


def test_analyze_rejects_invalid_file_type():
    client = TestClient(app)

    response = client.post(
        "/analyze",
        files={"eml_file": ("notes.txt", b"not an eml file", "text/plain")},
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
    assert "Medium phishing risk" in response.text
