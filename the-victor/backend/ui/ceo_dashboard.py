import streamlit as st
from datetime import datetime
from core.victor_core import victor

def show_ceo_dashboard():
    st.set_page_config(page_title="CEO Dashboard - The Victor", layout="wide")
    
    st.title("👑 CEO Dashboard - The Victor")
    st.subheader("AI Web Builder Control Center")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Victor Version", victor.version)
        st.metric("Projects Created", victor.total_projects)
    
    with col2:
        st.metric("System Status", "Online")
        st.metric("God Mode", "Enabled")
    
    with col3:
        st.metric("Uptime", "Active")
    
    st.divider()
    
    if st.button("🚀 สร้างเว็บใหม่", type="primary", use_container_width=True):
        st.success("Victor พร้อมรับคำสั่งแล้วครับ CEO")
    
    if st.button("📊 ดูสถานะ Victor"):
        st.json(victor.get_status())
    
    st.caption("The Victor v4.0 - Built for CEO muramasa1405-cloud")

# สำหรับทดสอบ
if __name__ == "__main__":
    show_ceo_dashboard()
