from pathlib import Path

from fastapi import FastAPI, File, Form, Request, UploadFile
from fastapi.responses import HTMLResponse, PlainTextResponse, Response
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.analyzer import analyze_email
from app.email_parser import parse_email_content
from app.settings import settings

BASE_DIR = Path(__file__).resolve().parent
PROJECT_DIR = BASE_DIR.parent
ALLOWED_EMAIL_FILE_SUFFIXES = {".eml"}
DEMO_SAMPLES = {
    "payroll-credential-theft": {
        "label": "Payroll Credential Theft",
        "description": "High-risk credential theft example",
        "path": PROJECT_DIR / "samples" / "phishing_test.eml",
    },
    "suspicious-invoice": {
        "label": "Suspicious Invoice",
        "description": "Medium-risk business email example",
        "path": PROJECT_DIR / "samples" / "business_invoice_medium.eml",
    },
    "safe-newsletter": {
        "label": "Safe Newsletter",
        "description": "Low-risk legitimate message example",
        "path": PROJECT_DIR / "samples" / "newsletter_safe.eml",
    },
}

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
async def index(request: Request) -> Response:
    return _render_index(request)


@app.get("/demo-samples/{sample_id}", response_class=PlainTextResponse)
async def demo_sample(sample_id: str) -> PlainTextResponse:
    sample = DEMO_SAMPLES.get(sample_id)
    if not sample:
        return PlainTextResponse("Demo sample not found.", status_code=404)

    return PlainTextResponse(sample["path"].read_text(encoding="utf-8"))


@app.post("/analyze", response_class=HTMLResponse)
async def analyze(
    request: Request,
    pasted_email: str = Form(default=""),
    eml_file: UploadFile | None = File(default=None),
) -> Response:
    raw_email = pasted_email.strip()

    if eml_file and eml_file.filename:
        if Path(eml_file.filename).suffix.lower() not in ALLOWED_EMAIL_FILE_SUFFIXES:
            return _render_index(
                request,
                error="Invalid file type. Upload a .eml email file or paste raw email content.",
                status_code=400,
            )

        uploaded_bytes = await eml_file.read()
        if len(uploaded_bytes) > settings.max_upload_bytes:
            return _render_index(
                request,
                error="Uploaded file is too large for the configured upload limit.",
                status_code=413,
            )

        raw_email = uploaded_bytes.decode("utf-8", errors="replace")
        if not raw_email.strip():
            return _render_index(
                request,
                error="Paste email content or upload a .eml file before analyzing.",
                status_code=400,
            )

    if not raw_email:
        return _render_index(
            request,
            error="Paste email content or upload a .eml file before analyzing.",
            status_code=400,
        )

    parsed_email = parse_email_content(raw_email)
    result = await analyze_email(parsed_email)

    return _render_index(
        request,
        result=result,
        success="Analysis completed successfully. Review the report and recommended actions below.",
    )


@app.get("/health")
async def health() -> dict[str, str | bool]:
    return {
        "status": "ok",
        "llm_provider": settings.llm_provider,
        "openai_configured": bool(settings.openai_api_key),
        "openai_model": settings.openai_model,
    }


def _render_index(
    request: Request,
    *,
    result: dict | None = None,
    error: str | None = None,
    success: str | None = None,
    status_code: int = 200,
) -> Response:
    return templates.TemplateResponse(
        name="index.html",
        request=request,
        context={
            "request": request,
            "result": result,
            "error": error,
            "success": success,
            "demo_samples": _demo_sample_context(),
        },
        status_code=status_code,
    )


def _demo_sample_context() -> list[dict[str, str]]:
    return [
        {
            "id": sample_id,
            "label": str(sample["label"]),
            "description": str(sample["description"]),
        }
        for sample_id, sample in DEMO_SAMPLES.items()
    ]
