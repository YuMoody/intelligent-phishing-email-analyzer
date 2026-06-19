$ErrorActionPreference = "Stop"

$versionOk = python -c "import sys; print(int(sys.version_info >= (3, 12)))"
if ($versionOk -ne "1") {
    Write-Error "This prototype requires Python 3.12 or newer. Install Python 3.12+, then rerun this script."
}

if (-not (Test-Path ".venv")) {
    python -m venv .venv
}

.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt

if (-not (Test-Path ".env")) {
    Copy-Item ".env.example" ".env"
    Write-Host "Created .env from .env.example. Add OPENAI_API_KEY before using OpenAI analysis."
}

python -m uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
