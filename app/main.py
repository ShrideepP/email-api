from fastapi import FastAPI, HTTPException
from app.models import EmailRequest, EmailResponse
from app.email_service import send_email

app = FastAPI(
    title="Email API",
    description="Send transactional emails via SMTP",
    version="1.0.0",
)

@app.get("/health")
async def health_check():
    return {"status": "ok"}

@app.post("/send", response_model=EmailResponse)
async def send_email_endpoint(payload: EmailRequest):
    try:
        await send_email(payload)
        return EmailResponse(success=True, message="Email sent successfully")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))