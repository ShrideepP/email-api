from pydantic import BaseModel, EmailStr
from typing import Optional

class EmailRequest(BaseModel):
    to: EmailStr
    subject: str
    body: str
    html_body: Optional[str] = None  # optional HTML version

class EmailResponse(BaseModel):
    success: bool
    message: str