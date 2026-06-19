from pathlib import Path

from app.analyzer import build_heuristic_report
from app.email_parser import parse_email_content


def test_phishing_sample_scores_high_enough():
    raw_email = Path("samples/phishing_test.eml").read_text(encoding="utf-8")
    parsed = parse_email_content(raw_email)
    report = build_heuristic_report(parsed)

    assert report["score"] >= 75
    assert report["severity"] == "High"
    assert parsed.urls
    assert parsed.attachment_names == ["Security_Update.zip"]


def test_safe_sample_scores_low():
    raw_email = Path("samples/safe_test.eml").read_text(encoding="utf-8")
    parsed = parse_email_content(raw_email)
    report = build_heuristic_report(parsed)

    assert report["score"] < 45
    assert report["severity"] == "Low"
