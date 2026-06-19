# Intelligent Phishing Email Analyzer

CSC482 Capstone Project II, Team 4

## Team Project Description

The Intelligent Phishing Email Analyzer is a web-based Security Operations Center
(SOC) support tool for quickly reviewing suspicious emails. A junior analyst can
upload a `.eml` file or paste raw email content, then receive a structured
analysis report that highlights phishing risk, suspicious indicators, extracted
URLs, attachment names, and a plain-language explanation of why the email may be
safe or malicious.

The prototype uses Python, FastAPI, email parsing libraries, heuristic scoring,
and optional LLM-based reporting. The goal is not to replace a security analyst,
but to speed up triage and make phishing indicators easier to understand.

## Team Members

| Team Member | Role | Description |
| --- | --- | --- |
| Yuuki | Team leader, repository owner, integration lead | Coordinates the project schedule, creates the GitHub repository, merges prototype source code, reviews pull requests, and keeps the team aligned with the CSC482 milestones. |
| Joseph | Backend and email parsing contributor | Focuses on `.eml` parsing, header extraction, attachment metadata, test cases, and improving the risk-scoring logic. |
| Bivaina | Frontend and reporting contributor | Focuses on the web interface, analyst workflow, report readability, documentation, and final demo preparation. |

## Current Prototype Features

- Accepts pasted email content.
- Accepts `.eml` file uploads.
- Extracts basic email artifacts for analysis.
- Produces a phishing risk score using transparent heuristics.
- Optionally calls an LLM API for a natural-language SOC analyst report.
- Includes sample safe and phishing emails for testing.
- Includes unit tests for parser, analyzer, and web routes.

## Install and Run

### Prerequisites

- Python 3.12 or newer
- Git
- VS Code
- GitHub account for each team member
- OpenAI API key if using LLM-assisted reports

### Windows PowerShell

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
Copy-Item .env.example .env
.\scripts\run_dev.ps1
```

### Ubuntu or Git Bash

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
cp .env.example .env
bash scripts/run_dev.sh
```

Open the app at:

```text
http://localhost:8000
```

If `OPENAI_API_KEY` is not set in `.env`, the prototype still runs with
heuristic-only analysis.

## GitHub Repository Setup Guide

This guide assumes everyone is new to Git and GitHub, but already has Git and VS
Code installed.

### 1. Create GitHub Accounts

Each team member should:

1. Go to `https://github.com`.
2. Create a free account.
3. Verify the account email address.
4. Tell Yuuki the GitHub username.

### 2. Team Leader Creates the Public Repository

Yuuki should:

1. Sign in to GitHub.
2. Select **New repository**.
3. Repository name: `intelligent-phishing-email-analyzer`.
4. Description: `CSC482 Team 4 capstone project web app for phishing email analysis`.
5. Choose **Public**.
6. Do not add a GitHub README if this local project already has one.
7. Create the repository.

### 3. Team Leader Publishes the Initial Prototype from VS Code

In VS Code:

1. Open the project folder.
2. Select **Source Control** from the left sidebar.
3. If VS Code asks to initialize a repository, select **Initialize Repository**.
4. Confirm `.env` and `.venv` are not staged because they are ignored.
5. Stage the project files.
6. Commit with this message:

```text
Initial phishing analyzer prototype
```

7. Select **Publish Branch** or **Add Remote**.
8. Connect the local folder to Yuuki's GitHub repository.
9. Push the `main` branch.

Command-line fallback:

```bash
git init
git add .
git commit -m "Initial phishing analyzer prototype"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/intelligent-phishing-email-analyzer.git
git push -u origin main
```

### 4. Invite Team Members

Yuuki should:

1. Open the GitHub repository.
2. Go to **Settings**.
3. Go to **Collaborators**.
4. Invite Joseph and Bivaina by GitHub username.
5. Ask both teammates to accept the invitation.

### 5. Each Team Member Clones the Repository in VS Code

Each teammate should:

1. Open VS Code.
2. Press `Ctrl+Shift+P`.
3. Search for **Git: Clone**.
4. Paste the GitHub repository URL.
5. Choose a local folder.
6. Open the cloned project in VS Code.
7. Create `.env` from `.env.example`.
8. Run the setup commands from the install section.

### 6. README Collaboration Exercise

Each team member should practice the GitHub workflow by editing this README.

1. Pull the latest `main` branch.
2. Create a branch:

```bash
git checkout -b add-yuuki-description
```

Use the team member's own name in the branch, such as
`add-joseph-description` or `add-bivaina-description`.

3. Edit the team member description or task list.
4. Stage and commit the change in VS Code.
5. Push the branch to GitHub.
6. Open a pull request.
7. Ask another teammate to review it.
8. Merge after review.
9. Everyone pulls the updated `main` branch.

## Weekly Milestones

| Week | Dates | Milestones Completed | Milestones To Be Completed |
| --- | --- | --- | --- |
| Week 1 | 6/1-6/5 | Team formed; project topic selected; lab setup started. | Confirm all teammates have accounts and local tools ready. |
| Week 2 | 6/8-6/12 | Initial FastAPI prototype created; sample emails added; project plan drafted; local setup scripts added. | Create public GitHub repository; invite teammates; verify everyone can run the app locally. |
| Week 3 | 6/15-6/19 | Basic parser, analyzer, templates, and tests available in the prototype. | Improve `.eml` parsing for nested MIME, malformed messages, and richer header extraction. |
| Week 4 | 6/22-6/26 | Initial URL extraction and risk scoring available. | Add URL normalization, suspicious domain checks, URL shortener checks, and structured IoC output. |
| Week 5 | 6/29-7/3 | Initial LLM report path available when API key is configured. | Improve prompts, require structured JSON responses, add prompt-injection defenses, and document API cost controls. |
| Week 6 | 7/6-7/10 | Basic web upload and pasted-content workflow available. | Improve UI, add analyst notes, add report export, and polish accessibility. |
| Week 7 | 7/13-7/17 | Deployment outline started. | Add Windows Server and Ubuntu service instructions, logging, upload limits, and authentication plan. |
| Week 8 | 7/20-7/28 | Final project structure and demo materials in progress. | Freeze final code, rehearse final demo, prepare presentation, document limitations and ethics. |

## Team Member Tasks

### Yuuki

Completed:

- Selected and coordinated Team 4 project topic.
- Prepared the initial prototype source code for repository setup.
- Created the initial project README structure.
- Added project planning and deployment documentation.

To complete:

- Create the public GitHub repository.
- Push the initial source code to `main`.
- Invite Joseph and Bivaina as collaborators.
- Review and merge teammate pull requests.
- Coordinate final demo script and presentation order.

### Joseph

Completed:

- Reviewed the project direction and backend responsibilities.
- Prepared to contribute parser and analyzer improvements through GitHub.

To complete:

- Add self-description updates through a README pull request.
- Improve email header parsing for SPF, DKIM, DMARC, Reply-To, Return-Path, and Received path.
- Add more realistic benign, suspicious, and phishing test samples.
- Expand unit tests for parser and analyzer behavior.
- Help document backend limitations and false-positive risks.

### Bivaina

Completed:

- Reviewed the project direction and frontend/reporting responsibilities.
- Prepared to contribute UI and documentation updates through GitHub.

To complete:

- Add self-description updates through a README pull request.
- Improve the report layout and analyst workflow.
- Add clearer indicator tables and severity labels.
- Help add export options for final reports.
- Help prepare screenshots and demo steps for the final presentation.

## Collaboration Rules

- Pull before starting new work.
- Work on a branch instead of directly on `main`.
- Keep commits small and clearly named.
- Open pull requests for review.
- Do not commit `.env`, API keys, `.venv`, logs, or uploaded private emails.
- Run tests before asking for review.
- Use GitHub Issues or the README task list to track weekly work.

## Useful Commands

Run tests:

```bash
pytest
```

Check app health after starting the server:

```text
http://localhost:8000/health
```

Sample emails:

- `samples/phishing_test.eml`
- `samples/safe_test.eml`

## Security and Privacy Notes

- Treat submitted email content as sensitive data.
- Do not upload real private emails unless permission is granted.
- Keep `.env` out of GitHub.
- Use test samples for class demos.
- Add authentication before exposing the app outside a lab network.
- Document false positives, false negatives, and ethical limitations in the final report.

## Related Documentation

- `TODO_MILESTONES.md`: Detailed semester backlog.
- `docs/deployment.md`: Windows Server 2025 and Ubuntu 24.04 deployment outline.
