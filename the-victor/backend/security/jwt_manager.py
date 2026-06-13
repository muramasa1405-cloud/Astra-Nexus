import jwt
import os
from datetime import datetime, timedelta
from typing import Dict, Any, Optional

class JWTManager:
    def __init__(self):
        self.secret_key = os.getenv("JWT_SECRET_KEY", "victor-super-secret-key-2026")
        self.algorithm = "HS256"
        self.token_expire_minutes = 60 * 24 * 7  # 7 วัน
        
    def create_token(self, user_data: Dict[str, Any]) -> str:
        """สร้าง JWT Token"""
        to_encode = user_data.copy()
        expire = datetime.utcnow() + timedelta(minutes=self.token_expire_minutes)
        to_encode.update({"exp": expire})
        
        encoded_jwt = jwt.encode(to_encode, self.secret_key, algorithm=self.algorithm)
        return encoded_jwt
    
    def verify_token(self, token: str) -> Optional[Dict[str, Any]]:
        """ตรวจสอบ JWT Token"""
        try:
            payload = jwt.decode(token, self.secret_key, algorithms=[self.algorithm])
            return payload
        except jwt.ExpiredSignatureError:
            return None
        except jwt.JWTError:
            return None
    
    def get_current_user(self, token: str) -> Optional[Dict[str, Any]]:
        """ดึงข้อมูลผู้ใช้จาก Token"""
        payload = self.verify_token(token)
        if payload:
            return {
                "user_id": payload.get("user_id"),
                "username": payload.get("username"),
                "role": payload.get("role", "user")
            }
        return None

# Singleton
jwt_manager = JWTManager()
