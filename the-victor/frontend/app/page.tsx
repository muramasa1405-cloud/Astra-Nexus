'use client';

import { useState } from 'react';
import ChatInterface from '@/components/ChatInterface';
import LivePreview from '@/components/LivePreview';
import VictorControls from '@/components/VictorControls';

export default function VictorBuilder() {
  const [prompt, setPrompt] = useState('');
  const [generatedCode, setGeneratedCode] = useState('');
  const [isBuilding, setIsBuilding] = useState(false);
  const [projectName, setProjectName] = useState('Untitled Project');

  const handleBuild = async () => {
    if (!prompt.trim()) return;
    setIsBuilding(true);
    try {
      const res = await fetch('/api/victor/build', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ prompt, projectName, mode: 'full' }),
      });
      const data = await res.json();
      setGeneratedCode(data.code || data.html);
    } catch (error) {
      console.error('Build failed', error);
    } finally {
      setIsBuilding(false);
    }
  };

  return (
    <div className="min-h-screen gradient-bg overflow-hidden">
      <header className="fixed top-0 left-0 right-0 z-50 glass border-b border-white/10">
        <div className="max-w-screen-2xl mx-auto px-8 py-5 flex items-center justify-between">
          <div className="flex items-center gap-4">
            <div className="text-4xl font-bold bg-gradient-to-r from-purple-400 via-cyan-400 to-pink-400 bg-clip-text text-transparent">Victor</div>
            <div className="text-sm text-gray-400">AI Web Builder</div>
          </div>
          <VictorControls projectName={projectName} setProjectName={setProjectName} />
        </div>
      </header>

      <div className="flex h-screen pt-20">
        <div className="w-5/12 border-r border-white/10 bg-[#111113]/80 p-8 overflow-auto">
          <ChatInterface 
            prompt={prompt} 
            setPrompt={setPrompt} 
            onBuild={handleBuild} 
            isBuilding={isBuilding} 
            projectName={projectName} 
          />
        </div>
        <div className="w-7/12 p-8 overflow-auto bg-[#0a0a0f]">
          <div className="mb-4 flex items-center justify-between">
            <h2 className="text-xl font-semibold">Live Preview</h2>
            <div className="text-xs text-emerald-400">● Connected to Victor Core</div>
          </div>
          <LivePreview code={generatedCode} />
        </div>
      </div>
    </div>
  );
}