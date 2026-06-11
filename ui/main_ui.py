import streamlit as st
from ui.ceo_dashboard import show_ceo_dashboard
from core.react_builder import ReactBuilder

def main_ui():
    # Lovable Style UI
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
        .stApp { background: linear-gradient(135deg, #0f0f23 0%, #1a1a2e 40%, #312e81 100%); background-size: 400% 400%; animation: gradientShift 18s ease infinite; }
        @keyframes gradientShift { 0% { background-position: 0% 50%; } 50% { background-position: 100% 50%; } 100% { background-position: 0% 50%; } }
        .main-header { font-size: 4rem; font-weight: 800; background: linear-gradient(90deg, #c084fc, #60a5fa, #22d3ee); -webkit-background-clip: text; -webkit-text-fill-color: transparent; text-align: center; margin: 1.5rem 0; }
        .subtitle { text-align: center; color: #c4d0ff; font-size: 1.45rem; margin-bottom: 3rem; }
        .card { background: rgba(255,255,255,0.07); border-radius: 28px; padding: 32px; border: 1px solid rgba(255,255,255,0.15); backdrop-filter: blur(20px); }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<h1 class="main-header">Victor</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">AI that builds like Lovable • Self-Evolving</p>', unsafe_allow_html=True)

    col1, col2 = st.columns([1, 3])
    
    with col1:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("🎛️ Control Panel")
        mode = st.selectbox("เลือกโหมด", ["🌐 Web Builder (Streamlit)", "⚛️ React Builder (Lovable Style)", "🔄 Self-Improvement", "👑 CEO Dashboard"])
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        prompt = st.text_area("อธิบายสิ่งที่อยากสร้าง", height=160, placeholder="เช่น: สร้างเว็บร้านขายเสื้อผ้าแนว Streetwear")

        if st.button("🚀 สร้างเลย + Live Preview", type="primary", use_container_width=True):
            if prompt.strip():
                with st.spinner("Victor กำลังสร้าง..."):
                    if "React" in mode:
                        builder = ReactBuilder()
                        result = builder.generate_nextjs_app(prompt)
                        st.success(f"สร้าง {result['framework']} สำเร็จ!")
                        st.code(result['code'], language='tsx')
                    else:
                        st.success("สร้าง Streamlit App สำเร็จ! (Live Preview กำลังพัฒนา)")
            else:
                st.warning("กรุณาใส่คำอธิบาย")

        if st.button("👑 เปิด CEO Dashboard", use_container_width=True):
            show_ceo_dashboard()
        st.markdown('</div>', unsafe_allow_html=True)
