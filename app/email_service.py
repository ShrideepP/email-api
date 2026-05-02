import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

from app.config import settings
from app.models import EmailRequest

def _get_gmail_service():
    creds = Credentials(
        token=None,
        refresh_token=settings.gmail_refresh_token,
        token_uri="https://oauth2.googleapis.com/token",
        client_id=settings.gmail_client_id,
        client_secret=settings.gmail_client_secret,
    )
    return build("gmail", "v1", credentials=creds)

async def send_email(payload: EmailRequest) -> None:
    msg = MIMEMultipart("alternative")
    msg["Subject"] = payload.subject
    msg["From"] = settings.gmail_sender
    msg["To"] = payload.to

    msg.attach(MIMEText(payload.body, "plain"))
    if payload.html_body:
        msg.attach(MIMEText(payload.html_body, "html"))

    raw = base64.urlsafe_b64encode(msg.as_bytes()).decode()

    service = _get_gmail_service()
    service.users().messages().send(
        userId="me",
        body={"raw": raw}
    ).execute()