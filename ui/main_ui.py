import streamlit as st
from ui.ceo_dashboard import show_ceo_dashboard

def main_ui():
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
        
        .stApp {
            background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
        }
        
        .main-header {
            font-size: 3.2rem;
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
        
        .prompt-box {
            background: rgba(255,255,255,0.95);
            border-radius: 20px;
            padding: 20px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        }
        
        .stTextArea textarea {
            font-size: 1.1rem;
            min-height: 140px !important;
        }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<h1 class="main-header">Victor</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">What will you build today?</p>', unsafe_allow_html=True)

    # ช่อง Prompt ใหญ่แบบ Lovable
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
                # ใส่ logic การสร้างที่นี่ภายหลัง
            else:
                st.warning("Please describe what you want to build")

    with col2:
        if st.button("👑 CEO Dashboard", use_container_width=True):
            show_ceo_dashboard()

    # Live Preview (ถ้ามี)
    if "current_preview" in st.session_state and st.session_state.current_preview:
        st.subheader("Live Preview")
        st.components.v1.html(st.session_state.current_preview, height=600)
