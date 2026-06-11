# ui/main_ui.py
import streamlit as st
from ui.premium_css import apply_premium_css
from config.settings import APP_VERSION, APP_TITLE, CEO_MASTER_KEY
from agents.web_builder import generate_web_with_preview
from agents.ceo_agent import ceo_dashboard

def main_ui():
    apply_premium_css()
    
    st.title(f"⚡ {APP_TITLE}")
    st.caption("Multi-Agent • Self-Improvement • Live Preview • CEO Control")

    # Sidebar
    with st.sidebar:
        st.header("🎛️ Control Panel")
        
        mode = st.selectbox(
            "เลือกโหมดการทำงาน",
            ["🌐 Web Builder", "👑 CEO Dashboard", "🧠 Self-Improvement", "🤖 Multi-Agent"],
            index=0
        )
        
        st.radio("🌍 ภาษา", ["ไทย", "English"], horizontal=True)
        
        st.divider()
        st.button("🚀 Self-Improve Now", use_container_width=True)
        st.button("🧹 Clear Memory", use_container_width=True)

    # Main Content
    if "Web Builder" in mode:
        prompt = st.text_area("อธิบายเว็บไซต์ที่ต้องการสร้าง", 
                            placeholder="เว็บขายของออนไลน์ สไตล์มินิมอล สีดำ-ทอง...", 
                            height=150)
        
        if st.button("🚀 สร้างเว็บ + Live Preview", type="primary", use_container_width=True):
            generate_web_with_preview(prompt)
    
    elif "CEO Dashboard" in mode:
        ceo_dashboard()
    
    elif "Self-Improvement" in mode:
        st.subheader("🧠 Self-Improvement")
        st.info("Victor กำลังพัฒนาตัวเองแบบอัตโนมัติ...")
    
    else:
        st.subheader("🤖 Multi-Agent System")
        st.info("ระบบ Multi-Agent กำลังพัฒนา (Child Agents)")

    st.caption(f"Victor {APP_VERSION} • Modular Structure • Running on Streamlit Cloud")
