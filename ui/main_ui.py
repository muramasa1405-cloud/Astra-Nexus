import streamlit as st
from ui.ceo_dashboard import show_ceo_dashboard
from core.llm_client import LLMClient

def main_ui():
    st.markdown("""
    <style>
        .stApp { background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%); }
        .main-header { font-size: 3.8rem; font-weight: 700; color: white; text-align: center; margin: 2rem 0 0.5rem 0; }
        .subtitle { text-align: center; color: #94a3b8; font-size: 1.4rem; margin-bottom: 3rem; }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<h1 class="main-header">Victor</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">What will you build today?</p>', unsafe_allow_html=True)

    # === Victor Core ===
    if "victor_core" not in st.session_state:
        from core.victor_core import VictorCore
        st.session_state.victor_core = VictorCore()

    victor = st.session_state.victor_core
    st.write(victor.get_status())

    col1, col2 = st.columns(2)
    with col1:
        if st.button("🌌 เปิด Victor Core (24h Evolution)", use_container_width=True):
            victor.start_evolution()
    with col2:
        if st.button("🛑 Emergency Shutdown", use_container_width=True):
            st.error(victor.shutdown())

    st.divider()

    # === LLM (Gemini) + Chat ===
    if "llm" not in st.session_state:
        st.session_state.llm = LLMClient()

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    prompt = st.text_area("พิมพ์คำสั่งหรือสิ่งที่อยากให้ Victor ทำ...", height=120, placeholder="เช่น: สร้างเว็บร้านขายเสื้อผ้าแนว Streetwear")

    if st.button("🚀 ส่งให้ Victor", type="primary"):
        if prompt.strip():
            with st.spinner("Victor กำลังคิด..."):
                response = st.session_state.llm.think(prompt)
                st.session_state.chat_history.append({"user": prompt, "victor": response})
        else:
            st.warning("กรุณาพิมพ์คำสั่ง")

    # แสดงประวัติแชท
    for msg in st.session_state.chat_history:
        st.write(f"**คุณ:** {msg['user']}")
        st.write(f"**Victor:** {msg['victor']}")
        st.divider()

    if st.button("👑 CEO Dashboard"):
        show_ceo_dashboard()
