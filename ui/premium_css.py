# ui/premium_css.py
import streamlit as st

def apply_premium_css():
    st.markdown("""
    <style>
        /* Premium Dark Theme */
        .stApp {
            background: linear-gradient(135deg, #0f0f23 0%, #1a1a2e 100%);
            color: #e0e0ff;
        }
        
        .main .block-container {
            padding-top: 2rem;
            max-width: 1400px;
        }
        
        h1, h2, h3 {
            color: #a5b4fc !important;
            font-family: 'Segoe UI', system-ui;
        }
        
        .stButton>button {
            background: linear-gradient(90deg, #6366f1, #8b5cf6);
            color: white;
            border-radius: 12px;
            border: none;
            padding: 12px 28px;
            font-weight: 600;
            transition: all 0.3s;
        }
        
        .stButton>button:hover {
            transform: translateY(-3px);
            box-shadow: 0 10px 20px rgba(99, 102, 241, 0.4);
        }
        
        .card {
            background: rgba(255,255,255,0.05);
            border-radius: 16px;
            padding: 20px;
            border: 1px solid rgba(165, 180, 252, 0.2);
            backdrop-filter: blur(10px);
        }
        
        .live-preview {
            border: 2px solid #6366f1;
            border-radius: 12px;
            overflow: hidden;
        }
    </style>
    """, unsafe_allow_html=True)
