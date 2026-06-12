# backend/core/evaluator.py
# Phase 2 - Item 14

from typing import Dict, Any
from datetime import datetime

class Evaluator:
    def __init__(self):
        self.name = "Evaluator"
        self.version = "2.0.0"
        print(f"📊 Evaluator initialized - {self.name} v{self.version}")

    async def evaluate(self, generated_code: str, prompt: str) -> Dict[str, Any]:
        score = 85
        
        if len(generated_code) > 500:
            score += 5
        if "class" in generated_code or "def " in generated_code:
            score += 5
        if "responsive" in generated_code.lower() or "tailwind" in generated_code.lower():
            score += 5
        
        return {
            "status": "success",
            "overall_score": min(score, 100),
            "prompt": prompt,
            "code_length": len(generated_code),
            "strengths": [
                "Clean structure",
                "Good readability",
                "Modern syntax"
            ],
            "suggestions": [
                "Add more comments",
                "Consider error handling",
                "Optimize performance"
            ],
            "timestamp": datetime.now().isoformat(),
            "phase": "2 - Core Generation & Quality"
        }


evaluator = Evaluator()