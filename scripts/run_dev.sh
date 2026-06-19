#!/usr/bin/env bash
set -euo pipefail

version_ok="$(python3 -c 'import sys; print(int(sys.version_info >= (3, 12)))')"
if [ "$version_ok" != "1" ]; then
  echo "This prototype requires Python 3.12 or newer. Install Python 3.12+, then rerun this script." >&2
  exit 1
fi

if [ ! -d ".venv" ]; then
  python3 -m venv .venv
fi

source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt

if [ ! -f ".env" ]; then
  cp .env.example .env
  echo "Created .env from .env.example. Add OPENAI_API_KEY before using OpenAI analysis."
fi

python -m uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
