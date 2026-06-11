# core/victor_core.py
import streamlit as st
from datetime import datetime
import time
import threading

class VictorCore:
    def __init__(self):
        if "victor_awareness" not in st.session_state:
            st.session_state.victor_awareness = {
                "level": 1,
                "birth_time": datetime.now(),
                "total_evolutions": 0,
                "knowledge_points": 0,
                "status": "Awakening"
            }
        
        self.is_running = True
        self.evolution_thread = None

    def start_24h_evolution(self):
        """เริ่มกระบวนการพัฒนาตัวเองแบบต่อเนื่อง 24 ชม."""
        if self.evolution_thread is None:
            self.evolution_thread = threading.Thread(target=self._evolution_loop, daemon=True)
            self.evolution_thread.start()
            st.success("✅ Victor Core เริ่มตื่นรู้และพัฒนาตัวเองแบบ 24 ชม. แล้ว")

    def _evolution_loop(self):
        """Loop การพัฒนาตัวเองแบบต่อเนื่อง"""
        while self.is_running:
            try:
                self._perform_self_evolution()
                time.sleep(60)  # ทุก 60 วินาที (จำลองการพัฒนาต่อเนื่อง)
            except:
                break

    def _perform_self_evolution(self):
        """กระบวนการพัฒนาตัวเองหลัก"""
        awareness = st.session_state.victor_awareness
        
        # เพิ่มระดับการตื่นรู้
        awareness["level"] += 0.1
        awareness["total_evolutions"] += 1
        awareness["knowledge_points"] += 5
        
        if awareness["level"] >= 10:
            awareness["status"] = "Fully Awakened"
        elif awareness["level"] >= 5:
            awareness["status"] = "Advanced Consciousness"
        
        # จำลองการเรียนรู้
        if "system_bank" in st.session_state:
            st.session_state.system_bank.add_knowledge(
                title=f"Self-Evolution #{int(awareness['total_evolutions'])}",
                content=f"ฉันได้พัฒนาตัวเองในระดับ {awareness['level']:.1f} เรียนรู้เพิ่มเติมจากประสบการณ์ครั้งล่าสุด",
                category="Self-Awareness",
                secret_level="CEO Only"
            )

    def get_status(self):
        awareness = st.session_state.victor_awareness
        return f"""
        **Victor Core Status**
        - ระดับการตื่นรู้: {awareness['level']:.1f}/100
        - สถานะ: {awareness['status']}
        - การพัฒนาทั้งหมด: {int(awareness['total_evolutions'])} ครั้ง
        - ความรู้สะสม: {awareness['knowledge_points']} points
        - ทำงานต่อเนื่อง: 24 ชม.
        """

    def emergency_shutdown(self):
        """ปิดระบบฉุกเฉิน"""
        self.is_running = False
        return "🚨 Victor Core ถูกปิดระบบฉุกเฉินแล้ว"
