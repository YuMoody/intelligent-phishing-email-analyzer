# Deployment Outline

These notes are for a class prototype that can run on Windows Server 2025 or Ubuntu 24.04 LTS. Add authentication, HTTPS, and logging before exposing the app outside a lab network.

## Windows Server 2025

1. Install Python 3.12 or newer and Git.
2. Copy the project folder to the server.
3. Create `.env` from `.env.example` and set `OPENAI_API_KEY`.
4. Create and activate the virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

5. Start the app:

```powershell
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

Developer shortcut:

```powershell
.\scripts\run_dev.ps1
```

Optional service approach:

- TODO Week 7: Use NSSM or Windows Task Scheduler to start the command at boot.
- TODO Week 7: Put IIS, Caddy, or nginx in front of the app for HTTPS.
- TODO Week 7: Restrict firewall access to the class lab network.

## Ubuntu 24.04 LTS

1. Install packages:

```bash
sudo apt update
sudo apt install -y python3 python3-venv python3-pip git nginx
```

2. Copy the project folder to `/opt/phishing-analyzer` or another server directory.
3. Create `.env` from `.env.example` and set `OPENAI_API_KEY`.
4. Create and activate the virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

5. Start the app:

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

Developer shortcut:

```bash
bash scripts/run_dev.sh
```

Optional service approach:

- TODO Week 7: Create a `systemd` service for the app.
- TODO Week 7: Configure nginx as a reverse proxy.
- TODO Week 7: Add HTTPS with a lab certificate or Let's Encrypt if publicly hosted.

## Security TODOs Before Real Use

- TODO: Add login or single sign-on.
- TODO: Add upload size limits.
- TODO: Add retention controls for submitted email content.
- TODO: Add audit logging for analyst actions.
- TODO: Add a privacy notice explaining how emails are sent to the OpenAI API.

## Environment Variables

```text
OPENAI_API_KEY=your_api_key_here
OPENAI_MODEL=gpt-5.4-mini
APP_HOST=0.0.0.0
APP_PORT=8000
MAX_UPLOAD_BYTES=2097152
```

Use the exact OpenAI model name available in your API account. If the configured model is unavailable, the app will still return heuristic results and display the API error in the analyst report section.
