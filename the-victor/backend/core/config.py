import os
from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    """การตั้งค่าทั้งหมดของ Victor"""
    
    # Application
    APP_NAME: str = "The Victor - AI Web Builder"
    APP_VERSION: str = "4.0"
    DEBUG: bool = True
    
    # Security
    CEO_SECRET_KEY: str = "ceofank140500"
    JWT_SECRET_KEY: str = "victor-jwt-secret-key-2026"
    JWT_EXPIRE_MINUTES: int = 60 * 24 * 7  # 7 วัน
    
    # Database
    DATABASE_URL: str = "sqlite:///./victor.db"
    VECTOR_DB_PATH: str = "./vector_db"
    
    # LLM / AI
    OPENAI_API_KEY: Optional[str] = None
    DEFAULT_MODEL: str = "gpt-4o"
    
    # WebSocket
    WS_HEARTBEAT_INTERVAL: int = 30
    
    # Backup
    BACKUP_DIR: str = "./backups"
    BACKUP_RETENTION_DAYS: int = 30
    
    class Config:
        env_file = ".env"
        case_sensitive = True

# Global settings instance
settings = Settings()

# Print config on startup (development only)
if settings.DEBUG:
    print(f"⚙️  Victor Config Loaded | Version: {settings.APP_VERSION}")
