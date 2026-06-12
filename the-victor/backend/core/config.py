# backend/core/config.py
# Phase 1 Complete

from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    APP_NAME: str = "The Victor"
    VERSION: str = "1.0.0"
    CEO_SECRET_KEY: str = "ceofank140500"
    GEMINI_API_KEY: Optional[str] = None
    DEBUG: bool = True
    MAX_TOKENS: int = 8192
    TEMPERATURE: float = 0.7
    SANDBOX_ENABLED: bool = True
    AUDIT_LOG_PATH: str = "logs/audit.log"
    
    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8'
        extra = "ignore"

settings = Settings()