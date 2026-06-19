# Semester TODO Milestones

Use this file as the team backlog for CSC482 Capstone Project II. Keep completed work visible by changing `TODO` to `DONE` and adding the teammate name/date.

## Week 2: Prototype Foundation

- TODO: Confirm every teammate can run the FastAPI app on their own machine.
- TODO: Confirm final API model name, budget limit, and fallback behavior when the API is unavailable.
- TODO: Assign repo ownership roles for Yuuki, Joseph, and Bivaina.
- TODO: Add a short demo workflow using the two sample emails.

## Week 3: Email Parsing and Data Extraction

- TODO: Improve parsing for nested MIME and malformed `.eml` messages.
- TODO: Extract SPF, DKIM, DMARC, Reply-To, Return-Path, Received path, and sender display name.
- TODO: Capture attachment MIME type, file extension, and file size.
- TODO: Add more unit tests with benign, suspicious, and phishing examples.

## Week 4: URL and IoC Analysis

- TODO: Normalize URLs and extract root domains.
- TODO: Detect URL shorteners, punycode, lookalike domains, suspicious TLDs, and mismatched link text.
- TODO: Add optional sandbox or threat-intelligence lookup behind a feature flag.
- TODO: Store IoCs in a structured format that can be exported.

## Week 5: Prompt Engineering and LLM Reports

- TODO: Add few-shot prompt examples for SOC-style analysis.
- TODO: Enforce JSON output from OpenAI responses and validate the schema.
- TODO: Add prompt-injection defenses so email content is treated only as evidence.
- TODO: Add cost controls, max token settings, and request metadata logging.

## Week 6: Web UI and Analyst Workflow

- TODO: Add report export to PDF, DOCX, or Markdown.
- TODO: Add analyst notes, final verdict, and reviewed-by fields.
- TODO: Add severity filters and a clearer IoC table.
- TODO: Improve accessibility, mobile layout, and form validation.

## Week 7: Deployment and Reliability

- TODO: Create a Windows Server 2025 service option.
- TODO: Create an Ubuntu 24.04 LTS `systemd` service option.
- TODO: Add logging, upload limits, and error monitoring.
- TODO: Add authentication before exposing the app outside a lab network.

## Week 8: Final Demo and Presentation

- TODO: Prepare at least three realistic email examples for the final demo.
- TODO: Compare heuristic-only output against OpenAI-assisted output.
- TODO: Document limitations, ethics, privacy, and false-positive risk.
- TODO: Freeze the final code and rehearse the live demo.

