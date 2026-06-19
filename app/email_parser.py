from __future__ import annotations

import re
from dataclasses import dataclass, field
from email import policy
from email.parser import Parser
from email.utils import parseaddr


URL_PATTERN = re.compile(r"https?://[^\s<>\")']+", re.IGNORECASE)


@dataclass
class ParsedEmail:
    subject: str = ""
    from_header: str = ""
    reply_to: str = ""
    return_path: str = ""
    to_header: str = ""
    date: str = ""
    authentication_results: str = ""
    received_headers: list[str] = field(default_factory=list)
    body_text: str = ""
    urls: list[str] = field(default_factory=list)
    attachment_names: list[str] = field(default_factory=list)

    @property
    def sender_email(self) -> str:
        return parseaddr(self.from_header)[1].lower()

    @property
    def sender_display_name(self) -> str:
        return parseaddr(self.from_header)[0]


def parse_email_content(raw_email: str) -> ParsedEmail:
    message = Parser(policy=policy.default).parsestr(raw_email)

    body_parts: list[str] = []
    attachment_names: list[str] = []

    if message.is_multipart():
        for part in message.walk():
            content_disposition = part.get_content_disposition()
            filename = part.get_filename()

            if filename:
                attachment_names.append(filename)
                continue

            if content_disposition == "attachment":
                continue

            if part.get_content_type() in {"text/plain", "text/html"}:
                body_parts.append(_safe_content(part))
    else:
        body_parts.append(_safe_content(message))

    body_text = "\n\n".join(part for part in body_parts if part).strip()

    # TODO Week 3: Preserve separate plain-text and HTML bodies for better link-text mismatch checks.
    # TODO Week 3: Add robust parsing for malformed messages collected from real inbox exports.
    parsed = ParsedEmail(
        subject=message.get("subject", ""),
        from_header=message.get("from", ""),
        reply_to=message.get("reply-to", ""),
        return_path=message.get("return-path", ""),
        to_header=message.get("to", ""),
        date=message.get("date", ""),
        authentication_results=message.get("authentication-results", ""),
        received_headers=message.get_all("received", []),
        body_text=body_text,
        urls=sorted(set(URL_PATTERN.findall(body_text))),
        attachment_names=attachment_names,
    )

    return parsed


def _safe_content(part) -> str:
    try:
        return part.get_content()
    except Exception:
        payload = part.get_payload(decode=True)
        if isinstance(payload, bytes):
            return payload.decode("utf-8", errors="replace")
        return str(payload or "")
