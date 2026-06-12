# backend/core/victor_core.py
import time
from typing import Dict, Any, Optional
from datetime import datetime

from config.settings import settings
from security.ceo_override import ceo_override
from utils.activity_logger import audit_log

class VictorCore:
    """
    Phase 1: Foundation
    Victor Core พื้นฐาน - จัดการคำสั่งและ CEO Override
    """
    
    def __init__(self):
        self.version = "1.0.0"
        self.phase = "1 - Foundation"
        self.start_time = time.time()
        self.total_commands = 0
        print(f"🚀 Victor Core Phase 1 v{self.version} เริ่มทำงาน")

    async def process(self, command: str, ceo_key: Optional[str] = None) -> Dict[str, Any]:
        self.total_commands += 1
        timestamp = datetime.now().isoformat()
        
        audit_log.log("COMMAND_RECEIVED", command, ceo_key_used=bool(ceo_key))

        if ceo_key:
            result = ceo_override.verify_ceo_key(ceo_key, command)
            if result.get("status") == "granted":
                audit_log.log("GOD_MODE_ACTIVATED", command)
                return {
                    "status": "success",
                    "mode": "GOD_MODE",
                    "message": "Victor อยู่ในโหมด CEO สูงสุด",
                    "command": command,
                    "timestamp": timestamp
                }

        return {
            "status": "success",
            "version": self.version,
            "phase": self.phase,
            "command": command,
            "message": "Victor Core Phase 1: ประมวลผลคำสั่งสำเร็จ"
        }

    def get_status(self) -> Dict:
        return {
            "version": self.version,
            "phase": self.phase,
            "uptime": round(time.time() - self.start_time, 2),
            "total_commands": self.total_commands,
            "status": "ACTIVE"
        }


victor = VictorCore()