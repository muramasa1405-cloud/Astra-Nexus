import hashlib
import os
from typing import Dict, Any
from utils.activity_logger import audit_log

class CEOPasswordManager:
    """
    ระบบจัดการรหัสผ่าน CEO
    เริ่มต้นด้วยรหัส ceofank140500
    สามารถเปลี่ยนรหัสผ่านหน้าเว็บได้ (ต้องยืนยันรหัสเก่า)
    """

    def __init__(self):
        # รหัสเริ่มต้น (สามารถเปลี่ยนได้ผ่านเว็บ)
        self.current_password_hash = self._hash_password("ceofank140500")
        self.password_file = "ceo_password.txt"
        self._load_password()

    def _hash_password(self, password: str) -> str:
        return hashlib.sha256(password.encode()).hexdigest()

    def _load_password(self):
        """โหลดรหัสจากไฟล์ (ถ้ามี)"""
        if os.path.exists(self.password_file):
            with open(self.password_file, "r") as f:
                self.current_password_hash = f.read().strip()

    def _save_password(self, password_hash: str):
        """บันทึกรหัสลงไฟล์"""
        with open(self.password_file, "w") as f:
            f.write(password_hash)
        self.current_password_hash = password_hash

    def verify_password(self, password: str) -> bool:
        """ตรวจสอบว่ารหัสที่ใส่ถูกต้องหรือไม่"""
        return self._hash_password(password) == self.current_password_hash

    def change_password(self, old_password: str, new_password: str) -> Dict[str, Any]:
        """เปลี่ยนรหัสผ่าน (ต้องใส่รหัสเก่า)"""
        if not self.verify_password(old_password):
            audit_log.log(
                event_type="CEO_PASSWORD_CHANGE_FAILED",
                message="พยายามเปลี่ยนรหัสผ่านด้วยรหัสเก่าที่ไม่ถูกต้อง",
                level="WARNING"
            )
            return {"status": "failed", "message": "รหัสผ่านเก่าไม่ถูกต้อง"}

        if len(new_password) < 6:
            return {"status": "failed", "message": "รหัสผ่านใหม่ต้องมีอย่างน้อย 6 ตัวอักษร"}

        new_hash = self._hash_password(new_password)
        self._save_password(new_hash)

        audit_log.log(
            event_type="CEO_PASSWORD_CHANGED",
            message="CEO เปลี่ยนรหัสผ่านสำเร็จ",
            level="CRITICAL"
        )

        return {
            "status": "success",
            "message": "เปลี่ยนรหัสผ่านสำเร็จแล้ว"
        }

# Global instance
ceo_password_manager = CEOPasswordManager()
