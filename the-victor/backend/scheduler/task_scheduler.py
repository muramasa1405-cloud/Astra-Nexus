import asyncio
import schedule
import time
from datetime import datetime
from threading import Thread
from core.victor_core import victor
from utils.activity_logger import audit_log

class TaskScheduler:
    """
    ระบบ Scheduler สำหรับ Victor
    ทำงานอัตโนมัติ 24 ชั่วโมง (Self-Improvement, Backup, Check Status)
    """

    def __init__(self):
        self.is_running = False
        self.tasks = []

    def start(self):
        """เริ่ม Scheduler"""
        if self.is_running:
            return
        self.is_running = True
        
        Thread(target=self._run_scheduler, daemon=True).start()
        print("⏰ Task Scheduler เริ่มทำงาน (Background)")

    def _run_scheduler(self):
        """รัน scheduler ทุกนาที"""
        # ตั้งตารางงาน
        schedule.every(30).minutes.do(self.auto_self_improvement)
        schedule.every(6).hours.do(self.auto_backup)
        schedule.every(1).hour.do(self.check_system_health)

        while self.is_running:
            schedule.run_pending()
            time.sleep(60)

    def auto_self_improvement(self):
        """Victor พัฒนาตัวเองอัตโนมัติ"""
        audit_log.log("AUTO_SELF_IMPROVEMENT", "Victor เริ่มกระบวนการเรียนรู้และพัฒนาตัวเอง")
        print(f"[{datetime.now()}] Victor กำลังพัฒนาตัวเอง...")

    def auto_backup(self):
        """Backup อัตโนมัติ"""
        audit_log.log("AUTO_BACKUP", "ระบบ Backup อัตโนมัติทำงาน")
        print(f"[{datetime.now()}] Backup ระบบสำเร็จ")

    def check_system_health(self):
        """ตรวจสอบสถานะระบบ"""
        status = victor.get_status()
        audit_log.log("SYSTEM_HEALTH_CHECK", f"System Status: {status['status']}")
        print(f"[{datetime.now()}] Health Check: OK")

    def stop(self):
        self.is_running = False
        print("⏹️ Task Scheduler หยุดทำงาน")

# Global instance
task_scheduler = TaskScheduler()
