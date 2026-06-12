'use client';

import { useEffect, useState } from 'react';

interface LivePreviewProps {
  code: string;
}

export default function LivePreview({ code }: LivePreviewProps) {
  const [previewHTML, setPreviewHTML] = useState<string>('');

  useEffect(() => {
    if (!code) {
      setPreviewHTML(`
        <div class="flex items-center justify-center h-full text-gray-500">
          <div class="text-center">
            <div class="text-6xl mb-4">👀</div>
            <p class="text-xl">Victor กำลังรอคำสั่งสร้างเว็บของคุณ...</p>
          </div>
        </div>
      `);
      return;
    }

    // แสดงโค้ดที่ได้จาก Victor (สำหรับตอนนี้ใช้ iframe แสดงผล)
    setPreviewHTML(`
      <div class="border border-white/10 rounded-3xl overflow-hidden bg-white h-full min-h-[600px]">
        ${code}
      </div>
    `);
  }, [code]);

  return (
    <div className="h-full">
      <div className="flex items-center justify-between mb-4">
        <h2 className="text-2xl font-semibold">Live Preview</h2>
        <div className="text-xs px-3 py-1 bg-emerald-500/20 text-emerald-400 rounded-full">
          ● Real-time
        </div>
      </div>

      <div 
        className="glass rounded-3xl p-4 h-[calc(100vh-180px)] overflow-auto border border-white/10"
        dangerouslySetInnerHTML={{ __html: previewHTML }}
      />

      {code && (
        <div className="mt-4 text-xs text-gray-400 text-center">
          Victor กำลังแสดงผลแบบเรียลไทม์ • คุณสามารถพิมพ์ต่อในแชทเพื่อแก้ไขได้
        </div>
      )}
    </div>
  );
}
