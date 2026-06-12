# backend/core/model_router.py
from typing import Dict

class ModelRouter:
    """
    Phase 2: Core Intelligence
    เลือกโมเดลที่เหมาสมกับงาน
    """
    
    def __init__(self):
        print("🔀 Model Router initialized (Phase 2)")

    def route(self, intent_type: str, complexity: str = "medium") -> Dict:
        if intent_type == "create_website":
            model = "gpt-4o" if complexity == "high" else "gpt-4o-mini"
        elif intent_type == "modify_code":
            model = "claude-3.5-sonnet"
        else:
            model = "gpt-4o-mini"
        
        return {
            "selected_model": model,
            "reason": f"เลือกตาม intent: {intent_type} และ complexity: {complexity}",
            "phase": "2 - Core Intelligence"
        }


model_router = ModelRouter()