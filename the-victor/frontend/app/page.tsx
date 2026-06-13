'use client';

import { useState } from 'react';
import ChatInterface from '@/components/ChatInterface';
import LivePreview from '@/components/LivePreview';
import VictorControls from '@/components/VictorControls';
import ProjectManager from '@/components/ProjectManager';
import History from '@/components/History';

export default function VictorBuilder() {
  const [prompt, setPrompt] = useState('');
  const [generatedCode, setGeneratedCode] = useState('');
  const [isBuilding, setIsBuilding] = useState(false);

  const handleBuild = async () => {
    if (!prompt.trim()) return;
    
    setIsBuilding(true);
    try {
      const res = await fetch('/api/victor/build', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ prompt, projectName: 'Untitled Project' }),
      });
      const data = await res.json();
      setGeneratedCode(data.code || data.html || '<div>Victor สร้างเว็บเสร็จแล้ว</div>');
    } catch (error) {
      console.error(error);
      setGeneratedCode('<div class="text-red-500">เกิดข้อผิดพลาด กรุณาลองใหม่</div>');
    } finally {
      setIsBuilding(false);
    }
  };

  return (
    <div className="min-h-screen gradient-bg overflow-hidden">
      {/* Header */}
      <header className="fixed top-0 left-0 right-0 z-50 glass border-b border-white/10">
        <div className="max-w-screen-2xl mx-auto px-8 py-5 flex items-center justify-between">
          <div className="flex items-center gap-4">
            <div className="text-4xl font-bold bg-gradient-to-r from-purple-400 via-cyan-400 to-pink-400 bg-clip-text text-transparent">
              Victor
            </div>
            <div className="text-sm text-gray-400">AI Web Builder</div>
          </div>

          <div className="flex items-center gap-3">
            <ProjectManager />
            <History />
            <VictorControls />
          </div>
        </div>
      </header>

      {/* Main Content */}
      <div className="flex h-screen pt-20">
        {/* Left Panel - Chat */}
        <div className="w-5/12 border-r border-white/10 bg-[#111113]/80 p-8 overflow-auto">
          <ChatInterface 
            prompt={prompt} 
            setPrompt={setPrompt} 
            onBuild={handleBuild} 
            isBuilding={isBuilding} 
          />
        </div>

        {/* Right Panel - Live Preview */}
        <div className="w-7/12 p-8 overflow-auto bg-[#0a0a0f]">
          <div className="mb-4 flex items-center justify-between">
            <h2 className="text-2xl font-semibold">Live Preview</h2>
            <div className="text-xs px-3 py-1 bg-emerald-500/20 text-emerald-400 rounded-full">
              ● Connected to Victor
            </div>
          </div>
          <LivePreview code={generatedCode} />
        </div>
      </div>
    </div>
  );
}
