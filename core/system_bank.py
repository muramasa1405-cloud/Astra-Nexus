# core/system_bank.py
import json
import os
from datetime import datetime

class SystemBank:
    def __init__(self, filepath="system_bank.json"):
        self.filepath = filepath
        self.knowledge = self._load_knowledge()

    def _load_knowledge(self):
        if os.path.exists(self.filepath):
            with open(self.filepath, "r", encoding="utf-8") as f:
                return json.load(f)
        return []

    def _save_knowledge(self):
        with open(self.filepath, "w", encoding="utf-8") as f:
            json.dump(self.knowledge, f, ensure_ascii=False, indent=2)

    def add_knowledge(self, title, content, category="ทั่วไป", secret_level="CEO Only"):
        entry = {
            "id": len(self.knowledge) + 1,
            "title": title,
            "content": content,
            "category": category,
            "secret_level": secret_level,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.knowledge.append(entry)
        self._save_knowledge()
        return f"✅ เพิ่มความรู้ '{title}' เรียบร้อยแล้ว"

    def search_knowledge(self, query):
        results = []
        for item in self.knowledge:
            if query.lower() in item["title"].lower() or query.lower() in item["content"].lower():
                results.append(item)
        return results

    def get_all_knowledge(self):
        return self.knowledge
