import streamlit as st

def lovable_style_ui():
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
        
        .stApp {
            background: linear-gradient(135deg, #0f0f23 0%, #1a1a2e 50%, #312e81 100%);
            background-size: 300% 300%;
            animation: gradient 12s ease infinite;
        }
        
        @keyframes gradient {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }
        
        .header {
            font-size: 3.5rem;
            font-weight: 700;
            background: linear-gradient(90deg, #c084fc, #60a5fa, #22d3ee);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-align: center;
            margin: 1rem 0;
        }
        
        .card {
            background: rgba(255,255,255,0.08);
            border-radius: 20px;
            padding: 28px;
            border: 1px solid rgba(255,255,255,0.15);
            backdrop-filter: blur(12px);
        }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<h1 class="header">Victor</h1>', unsafe_allow_html=True)
    st.markdown('<p style="text-align:center; color:#a5b4fc; font-size:1.4rem;">AI that builds like Lovable</p>', unsafe_allow_html=True)
