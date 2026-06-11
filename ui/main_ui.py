import streamlit as st
from ui.ceo_dashboard import show_ceo_dashboard

def main_ui():
    # UI Style
    st.markdown("""
    <style>
        .stApp { background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%); }
        .main-header { font-size: 3.8rem; font-weight: 700; color: white; text-align: center; margin: 2rem 0 0.5rem 0; }
        .subtitle { text-align: center; color: #94a3b8; font-size: 1.4rem; margin-bottom: 2rem; }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<h1 class="main-header">Victor</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">AI that builds like Lovable • Self-Evolving</p>', unsafe_allow_html=True)

    # === Victor Core ===
    if "victor_core" not in st.session_state:
        from core.victor_core import VictorCore
        st.session_state.victor_core = VictorCore()

    victor = st.session_state.victor_core

    # แสดงสถานะ
    st.write(victor.get_status())

    # ปุ่มควบคุม Core
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🌌 เปิด Victor Core (24h Evolution)", use_container_width=True, type="primary"):
            victor.start_evolution()

    with col2:
        if st.button("🛑 Emergency Shutdown", use_container_width=True):
            st.error(victor.shutdown())

    st.divider()

    # Prompt Input
    prompt = st.text_area(
        "", 
        placeholder="พิมพ์สิ่งที่อยากให้ Victor สร้าง เช่น สร้างเว็บร้านขายเสื้อผ้า...",
        height=140,
        label_visibility="collapsed"
    )

    col_a, col_b = st.columns(2)
    with col_a:
        if st.button("🚀 Build Now", type="primary", use_container_width=True):
            if prompt.strip():
                st.success("Victor กำลังสร้าง...")
            else:
                st.warning("กรุณาใส่สิ่งที่อยากสร้าง")

    with col_b:
        if st.button("👑 CEO Dashboard", use_container_width=True):
            show_ceo_dashboard()
