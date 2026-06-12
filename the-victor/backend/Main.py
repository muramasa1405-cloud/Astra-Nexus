from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from core.victor_core import victor
from ui.ceo_dashboard import show_ceo_dashboard
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
        "message": "🚀 The Victor AI Web Builder",
        "status": "Online",
        "version": victor.version,
        "ceo_mode": "Enabled"
    }

@app.post("/api/victor/build")
async def build_website(data: dict):
    """Victor สร้างเว็บตามคำสั่ง CEO"""
    prompt = data.get("prompt", "")
    project_name = data.get("project_name", "Untitled Project")
    
    result = await victor.build_website(prompt, project_name)
    return result

@app.get("/api/victor/status")
async def get_status():
    return victor.get_status()

@app.get("/ceo/dashboard")
async def ceo_dashboard():
    return show_ceo_dashboard()

if __name__ == "__main__":
    print("🔥 Starting The Victor AI Web Builder...")
    uvicorn.run(app, host="0.0.0.0", port=8000)
