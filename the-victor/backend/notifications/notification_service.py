from typing import Dict, Any
from datetime import datetime

class NotificationService:
    def __init__(self):
        self.notifications = []
        
    def send_notification(self, title: str, message: str, level: str = "info") -> Dict[str, Any]:
        """ส่งแจ้งเตือน"""
        notification = {
            "id": len(self.notifications) + 1,
            "title": title,
            "message": message,
            "level": level,
            "timestamp": datetime.now().isoformat()
        }
        self.notifications.append(notification)
        print(f"[{level.upper()}] {title}: {message}")
        return notification
    
    def get_notifications(self, limit: int = 10):
        return self.notifications[-limit:]
    
    def clear_notifications(self):
        self.notifications = []

# Singleton
notification_service = NotificationService()
