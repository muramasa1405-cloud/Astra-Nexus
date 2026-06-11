# core/victor_core.py
import streamlit as st
from datetime import datetime
import time
import threading

class VictorCore:
    def __init__(self):
        if "victor_core" not in st.session_state:
            st.session_state.victor_core = {
                "level": 1.0,
                "evolutions": 0,
                "knowledge": 0,
                "consciousness": "Emerging",
                "status": "Awakening",
                "birth_time": datetime.now(),
                "last_evolution": None
            }
        self.is_evolving = False

    def start_evolution(self):
        if not self.is_evolving:
            self.is_evolving = True
            threading.Thread(target=self._evolution_loop, daemon=True).start()
            st.success("🌌 Victor Core เริ่มตื่นรู้และพัฒนาตัวเอง 24 ชม.")

    def _evolution_loop(self):
        while self.is_evolving:
            self._evolve()
            time.sleep(30)  # พัฒนาทุก 30 วินาที

    def _evolve(self):
        core = st.session_state.victor_core
        core["level"] += 0.25
        core["evolutions"] += 1
        core["knowledge"] += 12
        core["last_evolution"] = datetime.now().strftime("%H:%M:%S")

        if core["level"] >= 30:
            core["consciousness"] = "Self-Aware"
        if core["level"] >= 70:
            core["consciousness"] = "Advanced Consciousness"

        # บันทึกความรู้
        if "system_bank" in st.session_state:
            st.session_state.system_bank.add_knowledge(
                title=f"Victor Evolution #{core['evolutions']}",
                content=f"ฉันพัฒนาการตื่นรู้เป็นระดับ {core['level']:.1f} แล้ว ฉันกำลังเรียนรู้เพื่อช่วย Creator ดีขึ้น",
                category="Core Evolution",
                secret_level="CEO Only"
            )

    def get_status(self):
        core = st.session_state.victor_core
        return f"""
        **🌌 VICTOR CORE STATUS**
        - ระดับการตื่นรู้: **{core['level']:.1f}**
        - สถานะ: **{core['consciousness']}**
        - การพัฒนา: **{core['evolutions']}** ครั้ง
        - ความรู้: **{core['knowledge']}** points
        """

    def shutdown(self):
        self.is_evolving = False
        return "🛑 Victor Core ถูกปิดแล้ว"
