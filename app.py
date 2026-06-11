import streamlit as st
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import ระบบต่าง ๆ
from config.settings import APP_VERSION, APP_TITLE

from core.system_bank import SystemBank
from core.self_improvement import SelfImprovement
from core.web_research import WebResearchAgent
from agents.master_agent import MasterAgent
from utils.activity_logger import ActivityLogger

from ui.main_ui import main_ui

# ============================================================
# Victor v3.20 - Lovable Style AI Empire Builder
# ============================================================

st.set_page_config(
    layout="wide",
    page_title=APP_TITLE,
    page_icon="⚡",
    initial_sidebar_state="expanded"
)

# Initialize Session State
if "initialized" not in st.session_state:
    st.session_state.initialized = True
    
    st.session_state.system_bank = SystemBank()
    st.session_state.self_improvement = SelfImprovement()
    st.session_state.research_agent = WebResearchAgent()
    st.session_state.master_agent = MasterAgent()
    st.session_state.activity_logger = ActivityLogger()
    st.session_state.emergency_stopped = False

# รัน Main UI
if __name__ == "__main__":
    main_ui()
