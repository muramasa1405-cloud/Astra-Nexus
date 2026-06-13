from typing import Dict, Any, Set
import asyncio
import secrets
from datetime import datetime, timedelta

class WebSocketManager:
    """
    ระบบ Real-time WebSocket พร้อม Authentication + Refresh Token
    """

    def __init__(self):
        self.active_connections: Set = set()
        self.authenticated_clients: Dict = {}
        self.refresh_tokens: Dict = {}
        print("⚡ WebSocket Manager + Refresh Token เปิดใช้งานแล้ว")

    async def connect(self, websocket):
        self.active_connections.add(websocket)
        await self.send_message(websocket, {
            "type": "welcome",
            "message": "Connected to Victor Real-time Server",
            "require_auth": True
        })

        try:
            while True:
                data = await websocket.receive_json()
                await self.handle_message(websocket, data)
        except:
            await self.disconnect(websocket)

    async def handle_message(self, websocket, data: Dict):
        action = data.get("action")

        if action == "auth":
            # รับ CEO Key จาก Client
            ceo_key = data.get("ceo_key")
            if ceo_key == "ceofank140500":  # ใช้ key จริงใน production
                access_token = secrets.token_hex(32)
                refresh_token = secrets.token_hex(48)

                user_info = {
                    "role": "ceo",
                    "authenticated_at": datetime.now().isoformat(),
                    "access_token": access_token,
                    "refresh_token": refresh_token,
                    "expires_at": datetime.now() + timedelta(minutes=30)
                }

                self.authenticated_clients[websocket] = user_info
                self.refresh_tokens[refresh_token] = user_info

                await self.send_message(websocket, {
                    "type": "auth_success",
                    "access_token": access_token,
                    "refresh_token": refresh_token,
                    "expires_in": 1800,
                    "message": "ยืนยันตัวตนสำเร็จ — CEO Mode"
                })
                return

        elif action == "refresh_token":
            refresh_token = data.get("refresh_token")
            if refresh_token in self.refresh_tokens:
                new_access_token = secrets.token_hex(32)
                new_refresh_token = secrets.token_hex(48)

                user_info = self.refresh_tokens[refresh_token]
                user_info["access_token"] = new_access_token
                user_info["refresh_token"] = new_refresh_token
                user_info["expires_at"] = datetime.now() + timedelta(minutes=30)

                self.refresh_tokens[new_refresh_token] = user_info

                await self.send_message(websocket, {
                    "type": "token_refreshed",
                    "access_token": new_access_token,
                    "refresh_token": new_refresh_token,
                    "expires_in": 1800
                })
                return

        if websocket not in self.authenticated_clients:
            await self.send_message(websocket, {"type": "error", "message": "กรุณายืนยันตัวตนก่อน"})
            return

        if action == "command":
            # ตัวอย่าง: ส่งคำสั่งไป Victor Core
            await self.send_message(websocket, {
                "type": "command_result",
                "message": "คำสั่งถูกประมวลผลแล้ว"
            })

    async def disconnect(self, websocket):
        self.active_connections.discard(websocket)
        if websocket in self.authenticated_clients:
            user = self.authenticated_clients.pop(websocket)
            if user.get("refresh_token"):
                self.refresh_tokens.pop(user["refresh_token"], None)

    async def send_message(self, websocket, message: Dict):
        try:
            await websocket.send_json(message)
        except:
            await self.disconnect(websocket)

    def is_authenticated(self, websocket) -> bool:
        return websocket in self.authenticated_clients


websocket_manager = WebSocketManager()
