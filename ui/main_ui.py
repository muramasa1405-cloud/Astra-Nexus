# วางในไฟล์ ui/main_ui.py หรือท้าย app.py
import streamlit as st

def lovable_ui():
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
    st.markdown('<p class="subtitle">The AI that builds like Lovable</p>', unsafe_allow_html=True)
