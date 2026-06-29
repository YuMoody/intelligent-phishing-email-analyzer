from pathlib import Path

from fastapi import FastAPI, File, Form, Request, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.analyzer import analyze_email
from app.email_parser import parse_email_content
from app.settings import settings

BASE_DIR = Path(__file__).resolve().parent
ALLOWED_EMAIL_FILE_SUFFIXES = {".eml"}

app = FastAPI(
    title="Intelligent Phishing Email Analyzer",
    description="SOC tool for automated phishing assessment and explanation.",
    version="0.1.0",
)

app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")
templates = Jinja2Templates(directory=BASE_DIR / "templates")
# TODO Week 7: Revisit template caching after the deployment Python version is finalized.
templates.env.cache = None


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(
        name="index.html",
        request=request,
        context={
            "request": request,
            "result": None,
            "error": None,
        },
    )


@app.post("/analyze", response_class=HTMLResponse)
async def analyze(
    request: Request,
    pasted_email: str = Form(default=""),
    eml_file: UploadFile | None = File(default=None),
):
    raw_email = pasted_email.strip()

    if eml_file and eml_file.filename:
        if Path(eml_file.filename).suffix.lower() not in ALLOWED_EMAIL_FILE_SUFFIXES:
            return templates.TemplateResponse(
                name="index.html",
                request=request,
                context={
                    "request": request,
                    "result": None,
                    "error": "Invalid file type. Upload a .eml email file or paste raw email content.",
                },
                status_code=400,
            )

        uploaded_bytes = await eml_file.read()
        if len(uploaded_bytes) > settings.max_upload_bytes:
            return templates.TemplateResponse(
                name="index.html",
                request=request,
                context={
                    "request": request,
                    "result": None,
                    "error": "Uploaded file is too large for the configured upload limit.",
                },
                status_code=413,
            )
        raw_email = uploaded_bytes.decode("utf-8", errors="replace")

    if not raw_email:
        return templates.TemplateResponse(
            name="index.html",
            request=request,
            context={
                "request": request,
                "result": None,
                "error": "Paste email content or upload a .eml file before analyzing.",
            },
            status_code=400,
        )

    parsed_email = parse_email_content(raw_email)
    result = await analyze_email(parsed_email)

    return templates.TemplateResponse(
        name="index.html",
        request=request,
        context={
            "request": request,
            "result": result,
            "error": None,
        },
    )


@app.get("/health")
async def health():
    return {
        "status": "ok",
        "openai_configured": bool(settings.openai_api_key),
        "openai_model": settings.openai_model,
    }
