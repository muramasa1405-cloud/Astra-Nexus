import streamlit as st
import os
import sys

# เพิ่ม path เพื่อ import จากโฟลเดอร์ย่อย
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import จาก modular structure
from ui.main_ui import main_ui
from config.settings import APP_VERSION, APP_TITLE

# ============================================================
# Victor v3.16 - Premium Modular AI Web Builder
# ============================================================

st.set_page_config(
    layout="wide",
    page_title=APP_TITLE,
    page_icon="⚡",
    initial_sidebar_state="expanded"
)

# รัน Main UI
if __name__ == "__main__":
    main_ui()
