'use client';

import { useState } from 'react';
import ChatInterface from '@/components/ChatInterface';
import LivePreview from '@/components/LivePreview';
import VictorControls from '@/components/VictorControls';

export default function VictorBuilder() {
  const [prompt, setPrompt] = useState('');
  const [generatedCode, setGeneratedCode] = useState('');
  const [isBuilding, setIsBuilding] = useState(false);

  const handleBuild = async () => {
    setIsBuilding(true);
    try {
      const res = await fetch('/api/victor/build', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ prompt }),
      });
      const data = await res.json();
      setGeneratedCode(data.code);
    } catch (error) {
      alert('เกิดข้อผิดพลาด: ' + error);
    } finally {
      setIsBuilding(false);
    }
  };

  return (
    <div className="min-h-screen bg-[#0a0a0f] text-white">
      <header className="fixed top-0 left-0 right-0 z-50 bg-black/80 backdrop-blur-md border-b border-white/10">
        <div className="max-w-7xl mx-auto px-6 py-4 flex items-center justify-between">
          <h1 className="text-4xl font-bold bg-gradient-to-r from-purple-400 to-cyan-400 bg-clip-text text-transparent">
            The Victor
          </h1>
          <VictorControls />
        </div>
      </header>

      <div className="flex h-screen pt-16">
        <div className="w-5/12 border-r border-white/10 p-8">
          <ChatInterface 
            prompt={prompt} 
            setPrompt={setPrompt} 
            onBuild={handleBuild} 
            isBuilding={isBuilding} 
          />
        </div>
        
        <div className="w-7/12 p-8">
          <LivePreview code={generatedCode} />
        </div>
      </div>
    </div>
  );
}
