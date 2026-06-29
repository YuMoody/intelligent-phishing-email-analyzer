from pathlib import Path

import pytest

from app.analyzer import build_heuristic_report
from app.email_parser import parse_email_content


@pytest.mark.parametrize(
    ("sample_name", "minimum_score", "expected_severity"),
    [
        ("phishing_test.eml", 75, "High"),
        ("credential_redirect_phish.eml", 75, "High"),
        ("business_invoice_medium.eml", 45, "Medium"),
    ],
)
def test_risky_samples_score_at_expected_severity(sample_name, minimum_score, expected_severity):
    raw_email = Path("samples", sample_name).read_text(encoding="utf-8")
    parsed = parse_email_content(raw_email)
    report = build_heuristic_report(parsed)

    assert report["score"] >= minimum_score
    assert report["severity"] == expected_severity
    assert report["indicators"]


@pytest.mark.parametrize("sample_name", ["safe_test.eml", "newsletter_safe.eml"])
def test_safe_samples_score_low(sample_name):
    raw_email = Path("samples", sample_name).read_text(encoding="utf-8")
    parsed = parse_email_content(raw_email)
    report = build_heuristic_report(parsed)

    assert report["score"] < 45
    assert report["severity"] == "Low"


def test_phishing_sample_extracts_urls_and_attachment_names():
    raw_email = Path("samples/phishing_test.eml").read_text(encoding="utf-8")
    parsed = parse_email_content(raw_email)

    assert parsed.urls == ["https://bit.ly/example-reset"]
    assert parsed.attachment_names == ["Security_Update.zip"]


def test_medium_invoice_sample_flags_reply_to_and_risky_attachment():
    raw_email = Path("samples/business_invoice_medium.eml").read_text(encoding="utf-8")
    parsed = parse_email_content(raw_email)
    report = build_heuristic_report(parsed)

    indicator_types = {indicator["type"] for indicator in report["indicators"]}

    assert parsed.reply_to == "billing-help@external-mail.example"
    assert parsed.attachment_names == ["invoice_details.html"]
    assert "Header mismatch" in indicator_types
    assert "Risky attachment" in indicator_types


def test_html_phishing_sample_extracts_suspicious_url():
    raw_email = Path("samples/credential_redirect_phish.eml").read_text(encoding="utf-8")
    parsed = parse_email_content(raw_email)
    report = build_heuristic_report(parsed)

    assert parsed.urls == ["https://secure-login-update-company-example.com@evil.example/reset"]
    assert any(
        indicator["type"] == "Suspicious URL format"
        and indicator["value"] == "https://secure-login-update-company-example.com@evil.example/reset"
        for indicator in report["indicators"]
    )
