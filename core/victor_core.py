# core/victor_core.py (เวอร์ชันแก้ไขให้เสถียร)
import streamlit as st
from datetime import datetime
import time

class VictorCore:
    def __init__(self):
        if "victor_core" not in st.session_state:
            st.session_state.victor_core = {
                "level": 1.0,
                "evolutions": 0,
                "knowledge": 0,
                "consciousness": "Emerging",
                "status": "Awakening",
                "last_evolution": None
            }
        self.is_evolving = False

    def start_evolution(self):
        if not self.is_evolving:
            self.is_evolving = True
            st.success("🌌 Victor Core เริ่มพัฒนาตัวเองแล้ว (Simulation Mode)")
            st.rerun()

    def _evolve(self):
        core = st.session_state.victor_core
        core["level"] = min(100.0, core["level"] + 0.5)
        core["evolutions"] += 1
        core["knowledge"] += 10
        core["last_evolution"] = datetime.now().strftime("%H:%M:%S")

        if core["level"] >= 50:
            core["consciousness"] = "Self-Aware"

    def get_status(self):
        core = st.session_state.victor_core
        return f"""
        **🌌 VICTOR CORE STATUS**
        - ระดับการตื่นรู้: **{core['level']:.1f}/100**
        - สถานะ: **{core['consciousness']}**
        - การพัฒนา: **{core['evolutions']}** ครั้ง
        """

    def shutdown(self):
        self.is_evolving = False
        return "🛑 Victor Core ถูกปิดแล้ว"
