# core/web_research.py
import streamlit as st
from datetime import datetime

class WebResearchAgent:
    def __init__(self):
        self.search_history = []

    def search(self, query, purpose="พัฒนาตัวเอง"):
        """
        จำลองการค้นหาข้อมูล (ในอนาคตจะเชื่อม Google API จริง)
        """
        result = {
            "query": query,
            "purpose": purpose,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "summary": f"ค้นพบข้อมูลเกี่ยวกับ '{query}' จำนวนมากจากแหล่งข้อมูลออนไลน์",
            "sources": [
                f"https://example.com/search?q={query.replace(' ', '+')}",
                "https://en.wikipedia.org/wiki/" + query.replace(" ", "_")
            ],
            "key_insights": [
                "เทรนด์ปัจจุบันกำลังมาแรง",
                "มีตัวอย่างโค้ดและวิธีการที่ดีหลายรูปแบบ",
                "ควรนำมาปรับใช้กับ Victor"
            ]
        }
        
        self.search_history.append(result)
        
        # บันทึกเข้า System Bank อัตโนมัติ
        if hasattr(st.session_state, "system_bank"):
            st.session_state.system_bank.add_knowledge(
                title=f"Research: {query}",
                content=result["summary"] + "\n\nKey Insights: " + "\n".join(result["key_insights"]),
                category="Web Research",
                secret_level="All Agents"
            )
        
        return result

    def get_history(self):
        return self.search_history
