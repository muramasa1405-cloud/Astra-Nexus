import hashlib
import time
import hmac
from datetime import datetime, timedelta
from typing import Dict, Any
from utils.activity_logger import audit_log

class CEOOverride:
    """
    CEO God Mode System - ระบบควบคุมสูงสุด
    Victor ไม่สามารถปฏิเสธคำสั่งจาก CEO ได้
    """

    def __init__(self):
        self.active_god_sessions = {}
        self.CEO_SECRET_KEY = "ceofank140500"  # เปลี่ยนเป็น key จริงใน production

    def _generate_signature(self, timestamp: str, command: str) -> str:
        message = f"{self.CEO_SECRET_KEY}|{timestamp}|{command}".encode()
        return hmac.new(self.CEO_SECRET_KEY.encode(), message, hashlib.sha256).hexdigest()[:16]

    def verify_ceo_key(self, provided_key: str, command: str = "") -> Dict[str, Any]:
        """
        ตรวจสอบ CEO Key
        รูปแบบ: ceofank140500-timestamp-signature
        """
        if not provided_key:
            return {"status": "denied", "reason": "No key provided"}

        try:
            parts = provided_key.split('-')
            if len(parts) < 3:
                return {"status": "denied", "reason": "Invalid key format"}

            timestamp_str = parts[1]
            signature = parts[2]

            current_time = int(time.time())
            key_timestamp = int(timestamp_str)

            # ตรวจสอบหมดอายุ (30 นาที)
            if current_time - key_timestamp > 1800:
                return {"status": "denied", "reason": "Key expired"}

            # ตรวจสอบลายเซ็น
            expected_sig = self._generate_signature(timestamp_str, command)

            if signature == expected_sig:
                session_id = f"god_{current_time}"
                self.active_god_sessions[session_id] = {
                    "start_time": current_time,
                    "command": command
                }

                audit_log.log(
                    event_type="CEO_GOD_MODE_ACTIVATED",
                    message=f"God Mode activated: {command[:80]}...",
                    level="CRITICAL"
                )

                return {
                    "status": "granted",
                    "mode": "god_mode",
                    "bypass_all": True,
                    "session_id": session_id,
                    "message": "✅ CEO God Mode Activated"
                }

            return {"status": "denied", "reason": "Invalid signature"}

        except Exception as e:
            return {"status": "denied", "reason": str(e)}

    def emergency_shutdown(self) -> Dict:
        """หยุด Victor ฉุกเฉิน"""
        audit_log.log("EMERGENCY_SHUTDOWN", "CEO initiated emergency shutdown", level="CRITICAL")
        return {
            "status": "shutdown_initiated",
            "message": "Victor has been emergency stopped by CEO"
        }

    def get_active_sessions(self):
        return self.active_god_sessions


# Global instance
ceo_override = CEOOverride()
