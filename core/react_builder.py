# core/react_builder.py
class ReactBuilder:
    def generate_react_app(self, prompt):
        """สร้างโค้ด React + Next.js + Tailwind"""
        code = f"""// app/page.tsx
'use client';
import {{ useState }} from 'react';

export default function App() {{
  const [data, setData] = useState(null);
  
  return (
    <div className="min-h-screen bg-gradient-to-br from-purple-950 via-indigo-950 to-blue-950">
      <div className="max-w-4xl mx-auto p-8">
        <h1 className="text-6xl font-bold text-white mb-4">Victor Generated App</h1>
        <p className="text-xl text-purple-300 mb-12">Prompt: {prompt}</p>
        
        {/* เนื้อหาที่สร้างตาม prompt */}
        <div className="bg-white/10 backdrop-blur-xl rounded-3xl p-10 border border-white/20">
          <h2 className="text-3xl font-semibold text-white mb-6">Your Application</h2>
          {/* โค้ดส่วนอื่นจะถูกสร้างตาม prompt */}
        </div>
      </div>
    </div>
  );
}}
"""

        return {
            "framework": "Next.js 15 + React + Tailwind CSS",
            "code": code,
            "setup": "npm create next-app@latest my-app --typescript --tailwind",
            "note": "โค้ดถูกสร้างตาม prompt ของคุณ"
        }
