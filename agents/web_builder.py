# agents/web_builder.py
import streamlit as st
from config.settings import APP_VERSION

def generate_web_with_preview(prompt, language="thai"):
    """สร้างเว็บ + แสดง Live Preview"""
    
    st.subheader("🌐 Victor Web Builder")
    
    if not prompt:
        st.warning("กรุณาใส่คำอธิบายเว็บที่ต้องการ")
        return None
    
    with st.spinner("Victor กำลังสร้างเว็บไซต์ + Live Preview..."):
        # เรียกใช้ Gemini (ในอนาคตจะเชื่อม core/victor_brain.py)
        generated_html = f"""
        <!DOCTYPE html>
        <html lang="th">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Victor Generated Site</title>
            <style>
                body {{ font-family: 'Segoe UI', sans-serif; margin: 0; padding: 0; background: linear-gradient(135deg, #667eea, #764ba2); color: white; min-height: 100vh; }}
                .container {{ max-width: 1200px; margin: 0 auto; padding: 40px; text-align: center; }}
            </style>
        </head>
        <body>
            <div class="container">
                <h1>🌟 เว็บไซต์ที่ Victor สร้างให้</h1>
                <p>{prompt}</p>
                <p><strong>เวอร์ชัน {APP_VERSION} • Live Preview</strong></p>
            </div>
        </body>
        </html>
        """
        
        # แสดง Live Preview
        st.markdown("### 📺 Live Preview")
        st.components.v1.html(generated_html, height=600, scrolling=True)
        
        # แสดงโค้ด
        with st.expander("📄 ดูโค้ด HTML ที่สร้าง"):
            st.code(generated_html, language="html")
        
        st.success("✅ สร้างเว็บสำเร็จ! คุณสามารถแก้ไข Prompt แล้วกดสร้างใหม่ได้")
        return generated_html
