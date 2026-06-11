# agents/master_agent.py
import streamlit as st
from datetime import datetime

class MasterAgent:
    def __init__(self):
        if "child_agents" not in st.session_state:
            st.session_state.child_agents = []

    def spawn_child(self, task, purpose):
        """สร้างตัวลูกเพื่อทำงานเฉพาะทาง"""
        child = {
            "id": len(st.session_state.child_agents) + 1,
            "task": task,
            "purpose": purpose,
            "status": "กำลังทำงาน",
            "started_at": datetime.now().strftime("%H:%M:%S")
        }
        st.session_state.child_agents.append(child)
        return f"✅ สร้าง Child Agent #{child['id']} สำหรับงาน: {task}"

    def get_all_children(self):
        return st.session_state.child_agents

    def kill_child(self, child_id):
        """หยุดตัวลูก"""
        st.session_state.child_agents = [c for c in st.session_state.child_agents if c["id"] != child_id]
        return f"🛑 หยุด Child Agent #{child_id} แล้ว"
