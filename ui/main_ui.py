import streamlit as st
from ui.ceo_dashboard import show_ceo_dashboard

def main_ui():
    # === Lovable Style UI ===
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
        
        .stApp {
            background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
        }
        
        .main-header {
            font-size: 3.8rem;
            font-weight: 700;
            color: white;
            text-align: center;
            margin: 2rem 0 0.5rem 0;
        }
        
        .subtitle {
            text-align: center;
            color: #94a3b8;
            font-size: 1.4rem;
            margin-bottom: 3rem;
        }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<h1 class="main-header">Victor</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">What will you build today?</p>', unsafe_allow_html=True)

    # === Victor Core Status ===
    if "victor_core" in st.session_state:
        victor = st.session_state.victor_core
        st.write(victor.get_detailed_status())

    col_core1, col_core2 = st.columns(2)
    with col_core1:
        if st.button("🌌 เปิด Victor Core (24h Evolution)", use_container_width=True):
            if "victor_core" in st.session_state:
                st.session_state.victor_core.start_24h_evolution()
            else:
                st.error("Victor Core ยังไม่ได้สร้าง")

    with col_core2:
        if st.button("🛑 Emergency Shutdown", use_container_width=True):
            if "victor_core" in st.session_state:
                st.error(st.session_state.victor_core.emergency_shutdown())

    # === Prompt Input ===
    prompt = st.text_area(
        "", 
        placeholder="Ask Victor to build a landing page, dashboard, AI agent, or anything you want...",
        height=160,
        label_visibility="collapsed"
    )

    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("🚀 Build Now", type="primary", use_container_width=True):
            if prompt.strip():
                st.success("Victor is building your app...")
            else:
                st.warning("Please describe what you want to build")

    with col2:
        if st.button("👑 CEO Dashboard", use_container_width=True):
            show_ceo_dashboard()

    # Live Preview
    if "current_preview" in st.session_state and st.session_state.current_preview:
        st.subheader("👀 Live Preview")
        st.components.v1.html(st.session_state.current_preview, height=600)
