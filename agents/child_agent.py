# agents/child_agent.py
from datetime import datetime

class ChildAgent:
    def __init__(self, agent_id, task):
        self.id = agent_id
        self.task = task
        self.status = "active"
        self.started_at = datetime.now().strftime("%H:%M:%S")

    def work(self):
        """จำลองการทำงานของตัวลูก"""
        return {
            "agent_id": self.id,
            "task": self.task,
            "progress": "80%",
            "result": f"กำลังดำเนินการ '{self.task}'...",
            "suggestion": "ควรพัฒนาเพิ่มเติมในส่วน..."
        }
