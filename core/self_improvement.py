# core/self_improvement.py
import streamlit as st
from datetime import datetime

class SelfImprovement:
    def __init__(self):
        if "improvement_log" not in st.session_state:
            st.session_state.improvement_log = []

    def analyze(self, task, performance_score, feedback=""):
        """วิเคราะห์ผลงานและเสนอการปรับปรุง"""
        suggestion = self._generate_suggestion(performance_score, feedback)
        
        entry = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "task": task,
            "score": performance_score,
            "feedback": feedback,
            "suggestion": suggestion,
            "status": "กำลังพัฒนา"
        }
        
        st.session_state.improvement_log.append(entry)
        
        # บันทึกเข้า System Bank
        if "system_bank" in st.session_state:
            st.session_state.system_bank.add_knowledge(
                title=f"Self-Improvement: {task}",
                content=suggestion,
                category="Self-Improvement",
                secret_level="All Agents"
            )
        
        return entry

    def _generate_suggestion(self, score, feedback):
        if score < 70:
            return "ควรปรับปรุงความละเอียดและความถูกต้องของโค้ด"
        elif score < 85:
            return "เพิ่มความเร็วและประสิทธิภาพของระบบ"
        else:
            return "ผลงานดีเยี่ยม ควรขยายความสามารถให้กว้างขึ้น"

    def get_history(self):
        return st.session_state.improvement_log
