# Semester TODO Milestones

Use this file as the team backlog for CSC482 Capstone Project II. Keep completed work visible by changing `TODO` to `DONE` and adding the teammate name/date.

## Week 1: Course Setup and Project Selection

Team checklist:

- TODO: Review the syllabus and capstone expectations.
- TODO: Set up the lab environment.
- TODO: Form Team 4 and confirm the phishing email analyzer topic.
- TODO: Document the initial project concept.

Individual checklist:

Yuuki:

- [ ] Confirm team formation and record member contact information.
- [ ] Lead topic discussion and capture the initial project concept.
- [ ] Set up weekly check-in expectations.

Joseph:

- [ ] Complete lab environment setup.
- [ ] Research email parsing options for `.eml` files.
- [ ] Share backend tool recommendations with the team.

Bivaina:

- [ ] Complete lab environment setup.
- [ ] Review possible UI patterns for file upload and pasted email input.
- [ ] Collect example layouts for the analysis report screen.

## Week 2: Prototype Foundation

- TODO: Confirm every teammate can run the FastAPI app on their own machine.
- TODO: Confirm final API model name, budget limit, and fallback behavior when the API is unavailable.
- TODO: Assign repo ownership roles for Yuuki, Joseph, and Bivaina.
- TODO: Add a short demo workflow using the two sample emails.

Individual checklist:

Yuuki:

- [ ] Finalize project plan, timeline, and weekly schedule.
- [ ] Assign responsibilities for frontend, backend, AI integration, and documentation.
- [ ] Create or organize the project repository/workspace.

Joseph:

- [ ] Select backend language/framework and parsing library.
- [ ] Draft backend endpoint plan for upload and pasted-content analysis.
- [ ] Document parser inputs, outputs, and expected error cases.

Bivaina:

- [ ] Select frontend structure and page layout.
- [ ] Draft wireframe for upload, paste input, parsed preview, and report output.
- [ ] Define report fields needed from backend and LLM output.

## Week 3: Email Parsing and Data Extraction

- TODO: Improve parsing for nested MIME and malformed `.eml` messages.
- TODO: Extract SPF, DKIM, DMARC, Reply-To, Return-Path, Received path, and sender display name.
- TODO: Capture attachment MIME type, file extension, and file size.
- TODO: Add more unit tests with benign, suspicious, and phishing examples.

Individual checklist:

Yuuki:

- [ ] Track prototype progress and remove blockers.
- [ ] Review initial workflow from input to backend connection.
- [ ] Update schedule based on actual progress.

Joseph:

- [ ] Build initial backend endpoint for email submission.
- [ ] Implement first-pass `.eml` parsing for sender, subject, body, and headers.
- [ ] Test parser with at least two safe sample emails.

Bivaina:

- [ ] Build first web interface for `.eml` upload.
- [ ] Add pasted email content input.
- [ ] Connect frontend submission flow to the backend endpoint.

## Week 4: URL and IoC Analysis

- TODO: Normalize URLs and extract root domains.
- TODO: Detect URL shorteners, punycode, lookalike domains, suspicious TLDs, and mismatched link text.
- TODO: Add optional sandbox or threat-intelligence lookup behind a feature flag.
- TODO: Store IoCs in a structured format that can be exported.

Individual checklist:

Yuuki:

- [ ] Run a mid-project review of parser output and feature scope.
- [ ] Confirm required report fields and success criteria.
- [ ] Maintain the shared task board or weekly status notes.

Joseph:

- [ ] Extract URLs, attachment names, Reply-To, and key header fields.
- [ ] Normalize parser output into a structured format for LLM analysis.
- [ ] Add invalid file/input handling and parser test cases.

Bivaina:

- [ ] Display parsed email preview in the interface.
- [ ] Add user feedback for invalid input and processing states.
- [ ] Review the UI with the team and record improvement notes.

## Week 5: Prompt Engineering and LLM Reports

- TODO: Add few-shot prompt examples for SOC-style analysis.
- TODO: Enforce JSON output from OpenAI responses and validate the schema.
- TODO: Add prompt-injection defenses so email content is treated only as evidence.
- TODO: Add cost controls, max token settings, and request metadata logging.

Individual checklist:

Yuuki:

- [ ] Coordinate LLM prompt review and scoring expectations.
- [ ] Check whether the project is still on track for final demo requirements.
- [ ] Start collecting material for final documentation.

Joseph:

- [ ] Integrate the selected LLM or mock-analysis fallback.
- [ ] Send structured parsed email data into the analysis prompt.
- [ ] Validate required output fields: score, risk level, IoCs, explanation, and recommendation.

Bivaina:

- [ ] Create UI components for phishing score, risk level, IoCs, and recommendations.
- [ ] Handle loading, error, and no-result states.
- [ ] Confirm frontend can render sample LLM responses cleanly.

## Week 6: Web UI and Analyst Workflow

- TODO: Add report export to PDF, DOCX, or Markdown.
- TODO: Add analyst notes, final verdict, and reviewed-by fields.
- TODO: Add severity filters and a clearer IoC table.
- TODO: Improve accessibility, mobile layout, and form validation.

Individual checklist:

Yuuki:

- [ ] Lead end-to-end workflow review.
- [ ] Check documentation progress and assign missing sections.
- [ ] Approve final report layout and demo path.

Joseph:

- [ ] Refine backend response formatting and API error handling.
- [ ] Improve prompt consistency using examples and required JSON fields.
- [ ] Support frontend needs for report display.

Bivaina:

- [ ] Polish report interface and responsive layout.
- [ ] Add clear visual grouping for summary, IoCs, URLs, headers, and recommendations.
- [ ] Test the full workflow in the browser with sample emails.

## Week 7: Deployment and Reliability

- TODO: Create a Windows Server 2025 service option.
- TODO: Create an Ubuntu 24.04 LTS `systemd` service option.
- TODO: Add logging, upload limits, and error monitoring.
- TODO: Add authentication before exposing the app outside a lab network.

Individual checklist:

Yuuki:

- [ ] Lead testing review and prioritize bug fixes.
- [ ] Assign final presentation sections and demo speaking roles.
- [ ] Compile project limitations and future improvement notes.

Joseph:

- [ ] Run parser and backend tests with legitimate and phishing examples.
- [ ] Fix backend bugs found during testing.
- [ ] Write backend/setup documentation for the user guide.

Bivaina:

- [ ] Test UI behavior across common screen sizes.
- [ ] Fix report display and usability issues found during testing.
- [ ] Draft screenshots or visuals for the presentation.

## Week 8: Final Demo and Presentation

- TODO: Prepare at least three realistic email examples for the final demo.
- TODO: Compare heuristic-only output against OpenAI-assisted output.
- TODO: Document limitations, ethics, privacy, and false-positive risk.
- TODO: Freeze the final code and rehearse the live demo.

Individual checklist:

Yuuki:

- [ ] Finalize submission checklist and confirm all deliverables.
- [ ] Lead demo rehearsal and timing practice.
- [ ] Prepare backup demo plan in case live services are unavailable.

Joseph:

- [ ] Freeze backend features and verify the demo dataset works.
- [ ] Prepare mock/fallback analysis output if API access fails.
- [ ] Review final technical documentation for accuracy.

Bivaina:

- [ ] Freeze frontend features and complete final UI polish.
- [ ] Capture backup screenshots of the complete workflow.
- [ ] Review final slides for visual consistency and report screenshots.

## Final Presentation: Jul 27-Jul 28

Team checklist:

- TODO: Present the problem, solution, architecture, and implementation.
- TODO: Demonstrate email input, analysis, and report output.
- TODO: Explain results, limitations, and future improvements.
- TODO: Answer instructor and class questions.

Individual checklist:

Yuuki:

- [ ] Introduce the project, problem, scope, and team roles.
- [ ] Guide the live or recorded demo flow.
- [ ] Answer schedule, project-management, and limitation questions.

Joseph:

- [ ] Explain backend parsing, LLM integration, and technical decisions.
- [ ] Support the demo if backend or API issues occur.
- [ ] Answer implementation and testing questions.

Bivaina:

- [ ] Explain the user interface and report design.
- [ ] Show how analysts review score, IoCs, and recommendations.
- [ ] Answer usability and frontend questions.
