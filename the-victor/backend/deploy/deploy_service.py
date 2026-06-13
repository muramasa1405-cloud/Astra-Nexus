import os
from datetime import datetime
from typing import Dict, Any

class DeployService:
    def __init__(self):
        self.deploy_history = []
        
    async def deploy_project(self, project_name: str, code: str, platform: str = "vercel") -> Dict[str, Any]:
        """จำลองการ Deploy โปรเจกต์"""
        
        deploy_id = f"deploy_{datetime.now().strftime('%Y%m%d%H%M%S')}"
        
        result = {
            "deploy_id": deploy_id,
            "project_name": project_name,
            "platform": platform,
            "status": "success",
            "url": f"https://{project_name.lower().replace(' ', '-')}.vercel.app",
            "deployed_at": datetime.now().isoformat(),
            "message": f"Deploy สำเร็จ! Victor ได้ deploy โปรเจกต์ {project_name} ไปยัง {platform}"
        }
        
        self.deploy_history.append(result)
        return result
    
    def get_deploy_history(self):
        return self.deploy_history

# Singleton
deploy_service = DeployService()
