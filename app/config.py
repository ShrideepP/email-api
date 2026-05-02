from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    gmail_client_id: str
    gmail_client_secret: str
    gmail_refresh_token: str
    gmail_sender: str  # your Gmail address

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

settings = Settings()