from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from core.victor_core import victor
from security.ceo_password_manager import ceo_password_manager
from utils.activity_logger import audit_log
import uvicorn

app = FastAPI(title="The Victor - AI Web Builder", version="4.0")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {
        "message": "🚀 The Victor AI Web Builder v4.0",
        "status": "Online",
        "ceo_mode": "Enabled"
    }

@app.post("/api/victor/build")
async def build_website(data: dict):
    """Victor สร้างเว็บ"""
    prompt = data.get("prompt", "")
    project_name = data.get("project_name", "Untitled Project")
    
    result = await victor.build_website(prompt, project_name)
    return result

@app.get("/api/victor/status")
async def get_status():
    return victor.get_status()

@app.post("/api/ceo/change-password")
async def change_password(data: dict):
    """เปลี่ยนรหัส CEO"""
    old = data.get("old_password")
    new = data.get("new_password")
    return ceo_password_manager.change_password(old, new)

if __name__ == "__main__":
    print("🔥 Starting The Victor...")
    uvicorn.run(app, host="0.0.0.0", port=8000)
