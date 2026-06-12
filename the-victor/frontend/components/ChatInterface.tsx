'use client';
import { useState } from 'react';

export default function ChatInterface({ prompt, setPrompt, onBuild, isBuilding, projectName }: any) {
  const [messages, setMessages] = useState<any[]>([
    { role: 'assistant', content: 'สวัสดีครับ CEO วันนี้ต้องการสร้างอะไรครับ?' }
  ]);

  const handleSend = async () => {
    if (!prompt.trim()) return;
    setMessages(prev => [...prev, { role: 'user', content: prompt }]);
    setPrompt('');
  };

  return (
    <div className="flex flex-col h-full">
      <div className="mb-6">
        <h1 className="text-5xl font-bold tracking-tighter bg-gradient-to-r from-purple-400 to-cyan-400 bg-clip-text text-transparent">The Victor</h1>
        <p className="text-gray-400 mt-2">AI Web Builder ที่ฉลาดที่สุด</p>
      </div>

      <div className="flex-1 overflow-auto mb-6 space-y-4 pr-4">
        {messages.map((msg, i) => (
          <div key={i} className={`flex ${msg.role === 'user' ? 'justify-end' : 'justify-start'}`}>
            <div className={`max-w-[80%] glass rounded-2xl px-5 py-3 ${msg.role === 'user' ? 'bg-purple-600/80' : 'bg-white/5'}`}>
              {msg.content}
            </div>
          </div>
        ))}
      </div>

      <div className="glass rounded-3xl p-2">
        <textarea
          value={prompt}
          onChange={(e) => setPrompt(e.target.value)}
          placeholder="พิมพ์สิ่งที่อยากสร้าง..."
          className="w-full bg-transparent resize-none focus:outline-none min-h-[120px] px-5 py-4 text-lg"
          onKeyDown={(e) => e.key === 'Enter' && !e.shiftKey && handleSend()}
        />
        <button
          onClick={onBuild}
          disabled={isBuilding || !prompt.trim()}
          className="w-full mt-2 bg-gradient-to-r from-purple-500 to-cyan-500 py-4 rounded-2xl font-semibold text-lg disabled:opacity-50">
          {isBuilding ? 'Victor กำลังสร้าง...' : '🚀 สร้างเว็บด้วย Victor'}
        </button>
      </div>
    </div>
  );
}