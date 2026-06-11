import streamlit as st
from ui.ceo_dashboard import show_ceo_dashboard

def main_ui():
    # === Lovable Style UI ===
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
            background: linear-gradient(90deg, #c084fc, #60a5fa, #22d3ee, #a5f3fc);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-align: center;
            margin: 1.5rem 0 0.5rem 0;
            text-shadow: 0 0 40px rgba(192, 132, 252, 0.6);
        }
        
        .subtitle {
            text-align: center;
            color: #c4d0ff;
            font-size: 1.35rem;
            margin-bottom: 2rem;
            font-weight: 500;
        }
        
        .card {
            background: rgba(255,255,255,0.07);
            border-radius: 24px;
            padding: 28px;
            border: 1px solid rgba(255,255,255,0.12);
            backdrop-filter: blur(16px);
            box-shadow: 0 10px 40px rgba(0,0,0,0.4);
        }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<h1 class="main-header">Victor</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">AI that builds like Lovable • Self-Evolving</p>', unsafe_allow_html=True)

    # ส่วน Live Preview
    if "current_preview" not in st.session_state:
        st.session_state.current_preview = None

    if st.session_state.current_preview:
        st.subheader("👀 Live Preview")
        st.components.v1.html(st.session_state.current_preview, height=700, scrolling=True)

    # Main Content
    col1, col2 = st.columns([1, 3])
    
    with col1:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("🎛️ Control Panel")
        mode = st.selectbox("เลือกโหมด", 
                          ["🌐 Web Builder", "🤖 AI Agent Builder", "🔄 Self-Improvement", "🔍 Research Mode", "👑 CEO Dashboard"])
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        prompt = st.text_area("อธิบายสิ่งที่อยากสร้าง", 
                            placeholder="เช่น: สร้างเว็บร้านขายเสื้อผ้าแนว Streetwear ที่มีระบบตะกร้าและชำระเงิน",
                            height=150)
        
        col_a, col_b = st.columns(2)
        with col_a:
            if st.button("🚀 สร้างเลย + Live Preview", type="primary", use_container_width=True):
                st.success("Victor กำลังสร้าง...")
                # เรียกระบบสร้างแอปที่นี่ในอนาคต
        with col_b:
            if st.button("👑 เปิด CEO Dashboard", use_container_width=True):
                show_ceo_dashboard()
        st.markdown('</div>', unsafe_allow_html=True)
