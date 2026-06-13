import json
import os
from datetime import datetime
from typing import Dict, Any, Optional
from pathlib import Path

class AuditLogger:
    """
    ระบบ Audit Log แบบ Immutable
    บันทึกทุกการกระทำของ Victor โดยเฉพาะคำสั่งจาก CEO
    """

    def __init__(self):
        self.log_dir = Path("logs")
        self.log_dir.mkdir(exist_ok=True)
        self.audit_file = self.log_dir / "audit.log"
        self.activity_file = self.log_dir / "activity.jsonl"

    def log(self, event_type: str, message: str,
            user_id: str = "CEO",
            params: Optional[Dict] = None,
            success: bool = True,
            level: str = "INFO"):
        """บันทึกกิจกรรมแบบปลอดภัย"""
        timestamp = datetime.utcnow().isoformat()

        log_entry = {
            "timestamp": timestamp,
            "event_type": event_type,
            "message": message,
            "user_id": user_id,
            "level": level,
            "success": success,
            "params": params or {}
        }

        # เขียนไฟล์ audit.log (มนุษย์อ่านได้)
        with open(self.audit_file, "a", encoding="utf-8") as f:
            f.write(f"[{timestamp}] [{level}] {event_type}: {message}\n")
            if params:
                f.write(f"  Params: {json.dumps(params, ensure_ascii=False)}\n")

        # เขียนไฟล์ activity.jsonl (เครื่องอ่านได้)
        with open(self.activity_file, "a", encoding="utf-8") as f:
            f.write(json.dumps(log_entry, ensure_ascii=False) + "\n")

        # แสดงใน console (development)
        if os.getenv("DEBUG", "true").lower() == "true":
            print(f"🔒 AUDIT [{level}] {event_type}: {message}")

    def get_recent_logs(self, limit: int = 50) -> list:
        """ดึง log ล่าสุดสำหรับ CEO Dashboard"""
        logs = []
        try:
            with open(self.activity_file, "r", encoding="utf-8") as f:
                for line in list(f)[-limit:]:
                    logs.append(json.loads(line))
        except:
            pass
        return logs


# Global instance
audit_log = AuditLogger()
