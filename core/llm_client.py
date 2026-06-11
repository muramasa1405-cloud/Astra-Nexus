# core/llm_client.py
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

class LLMClient:
    def __init__(self):
        self.api_key = os.getenv("GEMINI_API_KEY")
        if self.api_key:
            genai.configure(api_key=self.api_key)
            self.model = genai.GenerativeModel('gemini-2.5-flash')
        else:
            self.model = None

    def think(self, prompt, system_prompt="You are Victor, a helpful and intelligent AI builder."):
        if not self.model:
            return "❌ ยังไม่ได้ตั้งค่า Gemini API Key"

        try:
            response = self.model.generate_content(f"{system_prompt}\n\nUser: {prompt}")
            return response.text
        except Exception as e:
            return f"❌ Error: {str(e)}"

# Initialize
if "llm" not in st.session_state:
    st.session_state.llm = LLMClient()
