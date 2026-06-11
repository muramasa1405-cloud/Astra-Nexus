# config/secrets.py
import os
import streamlit as st

# Gemini API Key (ใส่ key ของคุณที่นี่)
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY") or st.secrets.get("GEMINI_API_KEY", "YOUR_GEMINI_KEY_HERE")

# CEO Master Key (สำรอง)
CEO_MASTER_KEY = "ceofank140500"

def get_gemini_key():
    return GEMINI_API_KEY
