# Backend Notes

## Backend Setup
- Install project dependencies.
- Run the backend using:
  python3 -m uvicorn app.main:app --reload

## API Usage
Endpoint:
POST /analyze

Supports:
- .eml file uploads
- Raw email input

Returns:
- Risk Score
- Risk Level
- IoCs
- URLs
- Recommendations

## Fallback Behavior
If the AI model is unavailable, the backend uses the built-in phishing analysis logic.

## Known Limitations
- Only .eml files are supported.
- Large uploads are rejected.
- Analysis depends on the email content provided.
