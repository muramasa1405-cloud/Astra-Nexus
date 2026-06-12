# backend/core/prompt_guardrail.py
from typing import Dict

class PromptGuardrail:
    """
    Phase 2: Core Intelligence
    ป้องกัน Prompt ที่อันตรายหรือไม่เหมาสม
    """
    
    def __init__(self):
        self.blocked_keywords = ["hack", "delete all", "rm -rf", "drop database", "shutdown"]
        print("🛡️ Prompt Guardrail initialized (Phase 2)")

    def validate(self, prompt: str) -> Dict:
        prompt_lower = prompt.lower()
        
        for keyword in self.blocked_keywords:
            if keyword in prompt_lower:
                return {
                    "safe": False,
                    "reason": f"พบคำสั่งอันตราย: {keyword}",
                    "action": "blocked"
                }
        
        return {
            "safe": True,
            "reason": "Prompt ปลอดภัย",
            "action": "allowed"
        }


prompt_guardrail = PromptGuardrail()