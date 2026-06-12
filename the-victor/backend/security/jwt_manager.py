# backend/security/jwt_manager.py
import jwt
import secrets
import hashlib
from datetime import datetime, timedelta
from typing import Dict, Optional

class JWTManager:
    def __init__(self):
        self.secret_key = secrets.token_hex(32)
        self.algorithm = "HS256"
        print("🔑 JWT Manager initialized")

    def create_access_token(self, ceo_key: str):
        payload = {"sub": "ceo", "exp": datetime.utcnow() + timedelta(minutes=30)}
        return jwt.encode(payload, self.secret_key, algorithm=self.algorithm)

jwt_manager = JWTManager()