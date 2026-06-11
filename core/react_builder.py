# core/react_builder.py
class ReactBuilder:
    def generate_nextjs_app(self, prompt):
        """สร้างโค้ด Next.js + Tailwind CSS แบบ Lovable Style"""
        
        code = f"""// app/page.tsx
'use client';
import {{ useState }} from 'react';

export default function VictorApp() {{
  return (
    <div className="min-h-screen bg-gradient-to-br from-[#0f0f23] via-[#1a1a2e] to-[#312e81] text-white">
      <div className="max-w-5xl mx-auto p-8">
        <h1 className="text-6xl font-bold text-center mb-4 bg-gradient-to-r from-purple-400 to-cyan-400 bg-clip-text text-transparent">
          Victor
        </h1>
        <p className="text-center text-xl text-gray-300 mb-12">Prompt: {prompt}</p>
        
        <div className="bg-white/10 backdrop-blur-xl rounded-3xl p-10 border border-white/20">
          <h2 className="text-3xl font-semibold mb-8">Your Application</h2>
          <p className="text-gray-400">กำลังพัฒนา React App ตาม Prompt ของคุณ...</p>
        </div>
      </div>
    </div>
  );
}}
"""

        return {
            "framework": "Next.js 15 + React + TypeScript + Tailwind CSS",
            "code": code,
            "setup": "npx create-next-app@latest my-app --typescript --tailwind --eslint",
            "note": "คัดลอกโค้ดไปวางในโปรเจกต์ Next.js ของคุณ"
        }
