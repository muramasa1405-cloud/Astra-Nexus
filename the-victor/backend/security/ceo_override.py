# backend/security/ceo_override.py
class CEOOverride:
    def __init__(self):
        self.secret_key = "ceofank140500"
        print("🔐 CEO Override initialized")

    def verify_ceo_key(self, key: str, action: str):
        if key and "ceofank140500" in key:
            return {"status": "granted", "action": action}
        return {"status": "denied"}

ceo_override = CEOOverride()