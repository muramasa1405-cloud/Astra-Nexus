@echo off
title Victor v3.16 - Premium AI Builder

echo ========================================
echo     Victor v3.16 กำลังเริ่มทำงาน...
echo ========================================

cd /d "%~dp0"

echo [1/3] กำลังตรวจสอบและติดตั้งไลบรารี...
pip install streamlit requests google-generativeai python-dotenv --quiet

echo [2/3] กำลังรัน Victor...
echo.
echo ถ้าไม่ขึ้นหน้าเว็บอัตโนมัติ ให้เปิดเบราว์เซอร์แล้วไปที่ http://localhost:8501
echo.

streamlit run app.py

pause