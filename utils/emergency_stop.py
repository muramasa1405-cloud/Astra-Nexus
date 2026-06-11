# utils/emergency_stop.py
import streamlit as st

def emergency_stop():
    st.error("🚨 EMERGENCY STOP ถูกกด!")
    st.warning("Victor ถูกหยุดการทำงานชั่วคราว")
    
    if st.button("🔄 Resume Victor"):
        st.success("Victor กลับมาทำงานต่อแล้ว")
        st.rerun()
