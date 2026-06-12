'use client';
import { useState } from 'react';

interface ChatInterfaceProps {
  prompt: string;
  setPrompt: (value: string) => void;
  onBuild: () => void;
  isBuilding: boolean;
}

export default function ChatInterface({ prompt, setPrompt, onBuild, isBuilding }: ChatInterfaceProps) {
  const [messages, setMessages] = useState([
    { role: 'assistant', content: 'สวัสดีครับ CEO วันนี้ต้องการให้ Victor สร้างเว็บอะไรครับ?' }
  ]);

  const handleSend = () => {
    if (!prompt.trim()) return;
    
    setMessages(prev => [...prev, { role: 'user', content: prompt }]);
    
    // ส่งไป Victor Core
    onBuild();
    
    setPrompt('');
  };

  return (
    <div className="flex flex-col h-full">
      <div className="mb-8">
        <h1 className="text-5xl font-bold tracking-tighter bg-gradient-to-r from-purple-400 via-cyan-400 to-pink-400 bg-clip-text text-transparent">
          The Victor
        </h1>
        <p className="text-gray-400 mt-3 text-lg">AI Web Builder ที่ฉลาดที่สุดสำหรับ CEO</p>
      </div>

      {/* Chat Messages */}
      <div className="flex-1 overflow-y-auto space-y-6 mb-6 pr-4">
        {messages.map((msg, index) => (
          <div key={index} className={`flex ${msg.role === 'user' ? 'justify-end' : 'justify-start'}`}>
            <div className={`max-w-[85%] px-6 py-4 rounded-3xl ${
              msg.role === 'user' 
                ? 'bg-gradient-to-r from-purple-600 to-violet-600' 
                : 'bg-white/10 border border-white/10'
            }`}>
              {msg.content}
            </div>
          </div>
        ))}
      </div>

      {/* Prompt Input Area */}
      <div className="glass rounded-3xl p-2 border border-white/10">
        <textarea
          value={prompt}
          onChange={(e) => setPrompt(e.target.value)}
          placeholder="พิมพ์สิ่งที่อยากสร้าง... (เช่น สร้างเว็บขายคอร์สออนไลน์พรีเมี่ยม)"
          className="w-full bg-transparent resize-y min-h-[110px] p-5 text-lg focus:outline-none"
          onKeyDown={(e) => {
            if (e.key === 'Enter' && !e.shiftKey) {
              e.preventDefault();
              handleSend();
            }
          }}
        />
        <button
          onClick={handleSend}
          disabled={isBuilding || !prompt.trim()}
          className="w-full mt-3 py-4 bg-gradient-to-r from-purple-500 to-cyan-500 hover:from-purple-600 hover:to-cyan-600 rounded-2xl font-semibold text-lg transition-all disabled:opacity-50"
        >
          {isBuilding ? "Victor กำลังสร้าง..." : "🚀 สร้างด้วย Victor"}
        </button>
      </div>
    </div>
  );
}
