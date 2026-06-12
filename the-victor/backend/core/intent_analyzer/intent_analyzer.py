# backend/core/intent_analyzer/intent_analyzer.py
from typing import Dict

class IntentAnalyzer:
    """
    Phase 2: Core Intelligence
    วิเคราะห์เจตนาของ CEO
    """
    
    def __init__(self):
        print("🧠 Intent Analyzer initialized (Phase 2)")

    async def analyze(self, command: str) -> Dict:
        intent = {
            "original_command": command,
            "intent_type": self._classify_intent(command),
            "confidence": 0.85,
            "entities": [],
            "phase": "2 - Core Intelligence"
        }
        return intent

    def _classify_intent(self, command: str) -> str:
        command_lower = command.lower()
        if any(word in command_lower for word in ["สร้าง", "build", "create", "ทำ"]):
            return "create_website"
        elif any(word in command_lower for word in ["แก้", "fix", "ปรับ", "change"]):
            return "modify_code"
        elif any(word in command_lower for word in ["วิเคราะห์", "analyze", "รายงาน"]):
            return "analyze"
        else:
            return "general_command"


intent_analyzer = IntentAnalyzer()