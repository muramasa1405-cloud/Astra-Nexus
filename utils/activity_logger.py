# utils/activity_logger.py
import streamlit as st
from datetime import datetime

class ActivityLogger:
    def __init__(self):
        if "activity_log" not in st.session_state:
            st.session_state.activity_log = []

    def log(self, action, detail=""):
        entry = {
            "time": datetime.now().strftime("%H:%M:%S"),
            "action": action,
            "detail": detail
        }
        st.session_state.activity_log.append(entry)

    def get_recent_logs(self, limit=10):
        return st.session_state.activity_log[-limit:]
