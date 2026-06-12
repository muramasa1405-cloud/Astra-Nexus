'use client';

import { useState } from 'react';

export default function VictorControls() {
  const [isGodMode, setIsGodMode] = useState(false);

  return (
    <div className="flex items-center gap-3">
      {/* Status */}
      <div className="flex items-center gap-2 bg-white/5 px-4 py-2 rounded-2xl border border-white/10">
        <div className="w-2 h-2 bg-emerald-400 rounded-full animate-pulse"></div>
        <span className="text-sm text-emerald-400">Victor Online</span>
      </div>

      {/* God Mode (CEO Override) */}
      <button
        onClick={() => setIsGodMode(!isGodMode)}
        className={`px-5 py-2 rounded-2xl text-sm font-medium transition-all flex items-center gap-2 ${
          isGodMode 
            ? 'bg-yellow-500 text-black' 
            : 'bg-white/10 hover:bg-white/20 border border-white/10'
        }`}
      >
        👑 {isGodMode ? 'GOD MODE ON' : 'CEO Mode'}
      </button>

      {/* Evolution Button */}
      <button className="px-5 py-2 rounded-2xl bg-gradient-to-r from-purple-600 to-violet-600 hover:from-purple-700 hover:to-violet-700 text-sm font-medium transition-all">
        ⚡ Evolution
      </button>

      {/* Deploy Button */}
      <button className="px-6 py-2 rounded-2xl bg-white text-black font-semibold hover:bg-gray-200 transition-all">
        🚀 Deploy Now
      </button>
    </div>
  );
}
