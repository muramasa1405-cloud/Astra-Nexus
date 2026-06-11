# core/self_improvement.py
import time
from datetime import datetime
import streamlit as st

class SelfImprovement:
    def __init__(self):
        if "improvement_log" not in st.session_state:
            st.session_state.improvement_log = []

    def analyze_and_improve(self, task_description, result_quality):
        """
        วิเคราะห์ผลงานและเสนอการปรับปรุง
        """
        improvement = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "task": task_description,
            "quality_score": result_quality,
            "suggestion": self._generate_suggestion(result_quality),
            "status": "เสนอการปรับปรุง"
        }
        st.session_state.improvement_log.append(improvement)
        return improvement

    def _generate_suggestion(self, score):
        if score < 70:
            return "ควรปรับปรุงคุณภาพการตอบและเพิ่มรายละเอียด"
        elif score < 85:
            return "สามารถพัฒนาความเร็วและความแม่นยำได้อีก"
        else:
            return "ผลงานดี ควรบันทึกเป็นความรู้และนำไปใช้ต่อ"

    def get_improvement_history(self):
        return st.session_state.improvement_log
