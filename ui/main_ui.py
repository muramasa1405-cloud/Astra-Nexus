import streamlit as st
from ui.ceo_dashboard import show_ceo_dashboard

def main_ui():
    # Lovable Style
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
        .stApp {
            background: linear-gradient(135deg, #0f0f23 0%, #1a1a2e 40%, #312e81 100%);
            background-size: 400% 400%;
            animation: gradientShift 15s ease infinite;
        }
        @keyframes gradientShift {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }
        .main-header {
            font-size: 3.8rem;
            font-weight: 800;
            background: linear-gradient(90deg, #c084fc, #60a5fa, #22d3ee);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-align: center;
            margin: 1.5rem 0 0.5rem 0;
        }
        .subtitle {
            text-align: center;
            color: #c4d0ff;
            font-size: 1.35rem;
            margin-bottom: 2rem;
        }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<h1 class="main-header">Victor</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">AI that builds like Lovable • Self-Evolving</p>', unsafe_allow_html=True)

    col1, col2 = st.columns([1, 3])
    with col1:
        st.subheader("🎛️ Control Panel")
        mode = st.selectbox("เลือกโหมด", ["🌐 Web Builder", "🤖 AI Agent Builder", "🔄 Self-Improvement", "👑 CEO Dashboard"])

    with col2:
        prompt = st.text_area("อธิบายสิ่งที่อยากสร้าง", height=140, placeholder="เช่น: สร้างเว็บร้านขายเสื้อผ้า...")
        if st.button("🚀 สร้างเลย + Live Preview", type="primary"):
            st.success("Victor กำลังสร้าง...")
        if st.button("👑 เปิด CEO Dashboard"):
            show_ceo_dashboard()
