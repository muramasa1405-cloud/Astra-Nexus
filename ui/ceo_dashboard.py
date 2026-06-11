# ui/ceo_dashboard.py
import streamlit as st

def show_ceo_dashboard():
    st.title("👑 CEO Control Center - Victor v3.18")
    st.caption("Real-time Monitoring & Control")

    col1, col2 = st.columns([3, 1])
    
    with col1:
        st.subheader("📊 กิจกรรมเรียลไทม์")
        if "activity_log" in st.session_state and st.session_state.activity_log:
            for log in reversed(st.session_state.activity_log[-8:]):
                st.write(f"**{log['time']}** {log['action']}")
                if log.get('detail'):
                    st.caption(log['detail'])
        else:
            st.info("ยังไม่มีกิจกรรม")

    with col2:
        st.subheader("🚨 Control")
        if st.button("🛑 หยุด Victor ทันที", type="primary", use_container_width=True):
            st.error("🚨 Victor ถูกหยุดการทำงานทั้งระบบ!")
            st.session_state.emergency_stopped = True
        
        if st.button("🔄 Resume Victor", use_container_width=True):
            st.success("Victor กลับมาทำงานปกติแล้ว")
            st.session_state.emergency_stopped = False

    st.divider()
    st.subheader("🔄 Self-Improvement Status")
    if "improvement_log" in st.session_state and st.session_state.improvement_log:
        for imp in reversed(st.session_state.improvement_log[-5:]):
            st.write(f"✅ {imp['task']}")
            st.caption(imp['suggestion'])
    else:
        st.info("ยังไม่มีรายการพัฒนาตัวเอง")
