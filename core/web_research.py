# core/web_research.py
import streamlit as st
from datetime import datetime

class WebResearchAgent:
    def __init__(self):
        if "research_history" not in st.session_state:
            st.session_state.research_history = []

    def research(self, query, purpose="พัฒนาตัวเอง"):
        """จำลองการค้นหาข้อมูล (ภายหลังจะเชื่อม Google API จริง)"""
        result = {
            "query": query,
            "purpose": purpose,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "summary": f"พบข้อมูลที่เกี่ยวข้องกับ '{query}' จำนวนมาก",
            "key_findings": [
                "เทรนด์ปัจจุบันกำลังมาแรงในปี 2026",
                "มีตัวอย่างโค้ดและวิธีการที่ดีหลายรูปแบบ",
                "ควรนำมาปรับใช้เพื่อพัฒนา Victor"
            ],
            "sources": [
                f"https://google.com/search?q={query.replace(' ', '+')}",
                "https://github.com/trending"
            ]
        }
        
        st.session_state.research_history.append(result)
        
        # บันทึกเข้า System Bank อัตโนมัติ
        if "system_bank" in st.session_state:
            st.session_state.system_bank.add_knowledge(
                title=f"Research: {query}",
                content=result["summary"],
                category="Web Research",
                secret_level="All Agents"
            )
        
        return result

    def get_history(self):
        return st.session_state.research_history
