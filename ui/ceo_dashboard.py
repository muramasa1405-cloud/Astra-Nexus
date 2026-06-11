# ui/ceo_dashboard.py
import streamlit as st
from datetime import datetime

def show_ceo_dashboard():
    st.title("👑 CEO Control Center")
    st.caption("Victor Activity Monitor & Control")

    # Activity Log
    st.subheader("📊 กิจกรรมเรียลไทม์")
    
    if "activity_log" in st.session_state and st.session_state.activity_log:
        for log in reversed(st.session_state.activity_log[-10:]):
            st.write(f"**{log['time']}** — {log['action']}")
            if log['detail']:
                st.caption(log['detail'])
    else:
        st.info("ยังไม่มีกิจกรรม")

    # Self-Improvement Log
    st.subheader("🔄 Self-Improvement Log")
    if "improvement_log" in st.session_state and st.session_state.improvement_log:
        for imp in reversed(st.session_state.improvement_log[-5:]):
            st.write(f"**{imp['timestamp']}** — {imp['task']}")
            st.caption(f"ข้อเสนอ: {imp['suggestion']}")
    else:
        st.info("ยังไม่มีรายการพัฒนาตัวเอง")

    # Emergency Stop
    st.subheader("🚨 Emergency Control")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🛑 หยุด Victor ทันที", type="primary"):
            st.error("🚨 Victor ถูกหยุดการทำงานทั้งหมด!")
            st.session_state.emergency_stopped = True
    with col2:
        if st.button("🔄 เริ่ม Victor ใหม่"):
            st.success("Victor กลับมาทำงานแล้ว")
            st.session_state.emergency_stopped = False

    st.caption("ระบบกำลังพัฒนา • Victor v3.18")
