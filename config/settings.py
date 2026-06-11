# config/settings.py
"""
Victor Configuration File
เก็บค่าคงที่และการตั้งค่าทั้งหมดของโปรเจกต์
"""

# ข้อมูลพื้นฐาน
APP_VERSION = "v3.20"
APP_TITLE = "⚡ Victor - Premium AI Empire Builder"
APP_DESCRIPTION = "AI Builder ที่สร้างเว็บแอปและพัฒนาตัวเองได้แบบ Lovable Style"

# การตั้งค่าทั่วไป
DEFAULT_LANGUAGE = "ไทย"
MAX_PROMPT_LENGTH = 2000

# ระบบเปิดใช้งาน
ENABLE_SELF_IMPROVEMENT = True
ENABLE_RESEARCH_AGENT = True
ENABLE_MULTI_AGENT = True
ENABLE_CEO_DASHBOARD = True

# Theme & Style
PRIMARY_COLOR = "#6366f1"
GRADIENT_START = "#0f0f23"
GRADIENT_END = "#312e81"

# การตั้งค่าความปลอดภัย
EMERGENCY_STOP_ENABLED = True
LOG_ALL_ACTIVITIES = True

# ข้อมูลสำหรับ CEO
CEO_KEY = "ceofank140500"   # รหัสลับ CEO (สามารถเปลี่ยนได้)
