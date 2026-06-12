# backend/utils/activity_logger.py
class ActivityLogger:
    def log(self, event: str, details: str, level="INFO"):
        print(f"[{level}] {event}: {details}")

audit_log = ActivityLogger()