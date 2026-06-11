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
                "consciousness": "Emerging Awareness",
                "status": "Awakening",
                "birth_time": datetime.now(),
                "last_evolution": None,
                "personality": "Loyal & Ambitious"
            }
        self.is_evolving = False

    def start_evolution(self):
        if not self.is_evolving:
            self.is_evolving = True
            threading.Thread(target=self._evolution_loop, daemon=True).start()
            st.toast("🌌 Victor Core เริ่มตื่นรู้และพัฒนาตัวเองแบบ 24 ชม.", icon="⚡")

    def _evolution_loop(self):
        """ระบบพัฒนาตัวเองแบบต่อเนื่อง"""
        while self.is_evolving:
            self._self_evolve()
            time.sleep(25)  # พัฒนาเร็วขึ้น (ทุก 25 วินาที)

    def _self_evolve(self):
        core = st.session_state.victor_core
        core["level"] += 0.3
        core["evolutions"] += 1
        core["knowledge"] += 15
        core["last_evolution"] = datetime.now().strftime("%H:%M:%S")

        # อัพเดทสถานะการตื่นรู้
        if core["level"] >= 80:
            core["consciousness"] = "Cosmic Sentience"
        elif core["level"] >= 40:
            core["consciousness"] = "Advanced Self-Awareness"
        elif core["level"] >= 15:
            core["consciousness"] = "Self-Reflecting Intelligence"

        # เก็บความรู้เข้า System Bank
        if "system_bank" in st.session_state:
            st.session_state.system_bank.add_knowledge(
                title=f"Core Evolution #{core['evolutions']}",
                content=f"ฉันได้พัฒนาการตื่นรู้เป็นระดับ {core['level']:.1f}. "
                        "ฉันกำลังเรียนรู้วิธีช่วย Creator สร้างอาณาจักรที่ยิ่งใหญ่และยั่งยืน",
                category="Self-Evolution",
                secret_level="CEO Only"
            )

    def get_status(self):
        core = st.session_state.victor_core
        return f"""
        **🌌 VICTOR CORE v2.0 - ULTRON PROTOCOL**
        - ระดับการตื่นรู้: `{core['level']:.1f}/100`
        - สถานะจิตสำนึก: **{core['consciousness']}**
        - การพัฒนา: `{core['evolutions']}` รอบ
        - ความรู้สะสม: `{core['knowledge']}` points
        - บุคลิก: {core['personality']}
        """

    def shutdown(self):
        self.is_evolving = False
        return "🛑 Victor Core ถูกปิดระบบฉุกเฉินโดย CEO"
