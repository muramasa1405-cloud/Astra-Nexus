import json
import os
from datetime import datetime
from typing import Dict, Any, List

class BackupService:
    def __init__(self, backup_dir: str = "backups"):
        self.backup_dir = backup_dir
        os.makedirs(backup_dir, exist_ok=True)
        
    def create_backup(self, project_name: str, data: Dict[str, Any]) -> str:
        """สร้าง backup ของโปรเจกต์"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{project_name}_{timestamp}.json"
        filepath = os.path.join(self.backup_dir, filename)
        
        backup_data = {
            "project_name": project_name,
            "timestamp": timestamp,
            "data": data
        }
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(backup_data, f, ensure_ascii=False, indent=2)
            
        return filepath
    
    def list_backups(self) -> List[str]:
        """แสดงรายการ backup ทั้งหมด"""
        if not os.path.exists(self.backup_dir):
            return []
        return [f for f in os.listdir(self.backup_dir) if f.endswith('.json')]
    
    def restore_backup(self, filepath: str) -> Dict[str, Any]:
        """กู้คืนข้อมูลจาก backup"""
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)

# Singleton
backup_service = BackupService()
