'use client';

import { useState } from 'react';

interface HistoryItem {
  id: string;
  name: string;
  prompt: string;
  date: string;
}

export default function History() {
  const [history, setHistory] = useState<HistoryItem[]>([
    {
      id: '1',
      name: 'เว็บพอร์ตโฟลิโอ',
      prompt: 'สร้างเว็บพอร์ตโฟลิโอสไตล์พรีเมี่ยม',
      date: '2026-06-12'
    },
    {
      id: '2',
      name: 'เว็บขายสินค้า',
      prompt: 'สร้างเว็บอีคอมเมิร์ซที่สวยงาม',
      date: '2026-06-11'
    }
  ]);

  const [isOpen, setIsOpen] = useState(false);

  return (
    <div className="relative">
      <button
        onClick={() => setIsOpen(!isOpen)}
        className="px-4 py-2 bg-white/10 hover:bg-white/20 rounded-2xl text-sm border border-white/10 flex items-center gap-2 transition-all"
      >
        📜 ประวัติการสร้าง
      </button>

      {isOpen && (
        <div className="absolute right-0 mt-2 w-96 glass rounded-3xl p-4 border border-white/10 z-50 max-h-[500px] overflow-auto">
          <h3 className="font-semibold mb-4 text-lg">ประวัติการสร้างเว็บ</h3>
          
          {history.length === 0 ? (
            <p className="text-gray-400 text-sm">ยังไม่มีประวัติ</p>
          ) : (
            <div className="space-y-3">
              {history.map((item) => (
                <div 
                  key={item.id}
                  className="p-4 bg-white/5 rounded-2xl hover:bg-white/10 cursor-pointer border border-white/5 transition-all"
                >
                  <div className="flex justify-between items-start">
                    <div>
                      <div className="font-medium">{item.name}</div>
                      <div className="text-xs text-gray-400 mt-1 line-clamp-2">{item.prompt}</div>
                    </div>
                    <div className="text-xs text-gray-500 whitespace-nowrap ml-4">
                      {item.date}
                    </div>
                  </div>
                </div>
              ))}
            </div>
          )}
        </div>
      )}
    </div>
  );
}
