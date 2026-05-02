import aiosmtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from app.config import settings
from app.models import EmailRequest

async def send_email(payload: EmailRequest) -> None:
    msg = MIMEMultipart("alternative")
    msg["Subject"] = payload.subject
    msg["From"] = settings.smtp_from
    msg["To"] = payload.to

    # Plain text is always included; HTML is optional
    msg.attach(MIMEText(payload.body, "plain"))
    if payload.html_body:
        msg.attach(MIMEText(payload.html_body, "html"))

    await aiosmtplib.send(
        msg,
        hostname=settings.smtp_host,
        port=settings.smtp_port,
        username=settings.smtp_username,
        password=settings.smtp_password,
        start_tls=True,  # STARTTLS on port 587
    )