# Analysis Approach, Workflow, and Limitations

This document explains how the current prototype analyzes suspicious emails and
where its results should be treated cautiously. It is written for the CSC482
final report, demo preparation, and future implementation planning.

## Approach

The Intelligent Phishing Email Analyzer uses a layered analysis approach. The
goal is to give a junior SOC analyst a fast, readable first-pass assessment
without hiding the evidence that produced the result.

1. Email intake

   The web interface accepts either an uploaded `.eml` file or pasted raw email
   content. When both are provided, the uploaded file is used because exported
   `.eml` messages usually preserve more headers and MIME structure than copied
   text.

2. Parsing and artifact extraction

   The parser reads message headers, body text, URLs, and attachment filenames.
   Important fields include `Subject`, `From`, `Reply-To`, `Return-Path`,
   `To`, `Date`, `Authentication-Results`, and `Received` headers. The parser
   also walks multipart messages so text and HTML bodies can be reviewed.

3. Heuristic scoring

   The analyzer applies transparent rules to produce a 0-100 phishing risk
   score. Current indicators include suspicious language, Reply-To mismatches,
   authentication failures, shortened URLs, unusual URL formatting, and risky
   attachment extensions. Scores are mapped into low, medium, or high severity
   so analysts can quickly prioritize review.

4. IoC collection

   Observable artifacts are collected into the report as indicators of
   compromise. These can include sender addresses, URLs, attachment names, and
   rule-triggering values. The prototype focuses on evidence visible in the
   email rather than making unsupported claims about external infrastructure.

5. Analyst explanation

   The app can optionally call an LLM provider to generate a concise SOC-style
   explanation and recommended actions. The prompt asks for valid JSON, uses the
   parsed email and heuristic findings as evidence, and treats the email body as
   untrusted content. If no API key is configured or the provider fails, the app
   returns a deterministic mock analyst report so the demo remains usable.

## Analyst Workflow

1. Collect the suspicious message from the ticket queue, mailbox export, or
   class sample set.
2. Upload the `.eml` file, or paste the raw email source with headers when an
   exported file is not available.
3. Submit the message for analysis.
4. Review the parsed preview first to confirm the system extracted the expected
   sender, subject, recipients, URLs, and attachments.
5. Check the risk score and severity label to decide whether the message needs
   immediate escalation.
6. Review each listed indicator and compare it with the original email. The
   indicator table should explain what was detected and why it matters.
7. Read the analyst report for a plain-language summary and recommended next
   steps.
8. For medium or high risk messages, validate suspicious URLs and attachments in
   an approved sandbox or escalation process before taking blocking action.
9. Record the final analyst decision outside the prototype, such as in a SOC
   ticket, project demo notes, or incident-response queue.

## Limitations

The current prototype is a decision-support tool, not an automated verdict
engine. Its output should help prioritize review, but a human analyst should
make the final call.

- The heuristic weights are prototype values and have not been calibrated
  against a large labeled phishing dataset.
- URL checks are limited to visible URL structure, shortener detection, and
  simple formatting signals. The app does not currently follow redirects, check
  live reputation feeds, inspect domain age, or open links in a sandbox.
- Attachment analysis is based on filenames and extensions only. The app does
  not detonate attachments, compute hashes, scan file contents, or inspect
  macros.
- Email authentication handling depends on headers already present in the
  submitted message. Missing or incomplete `Authentication-Results` headers can
  reduce confidence.
- HTML parsing is basic. The app does not yet compare link text with actual
  destinations or fully preserve separate plain-text and HTML bodies.
- LLM-generated explanations can be incomplete or incorrect, especially when
  the parsed evidence is sparse. The heuristic report and original email should
  remain the primary evidence.
- Submitted emails may contain sensitive personal or organizational data. Real
  emails should not be used in demos unless permission has been granted.
- The prototype does not include authentication, role-based access control,
  audit logging, retention controls, or production-grade privacy controls.
- False positives and false negatives are expected. Benign security alerts,
  invoices, newsletters, and password-reset emails may contain language or links
  that resemble phishing patterns.

## Planned Improvements

- Calibrate scoring with a larger benign, suspicious, and phishing sample set.
- Add richer URL normalization, redirect inspection, and reputation checks.
- Preserve and analyze HTML-specific signals such as mismatched link text.
- Add report export so analysts can attach findings to tickets.
- Add authentication, upload retention limits, audit logging, and deployment
  hardening before any real SOC use.
