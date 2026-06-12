'use client';

export default function LivePreview({ code }: { code: string }) {
  if (!code) {
    return (
      <div className="h-[600px] flex items-center justify-center glass rounded-3xl">
        <div className="text-center">
          <div className="text-6xl mb-4">🔮</div>
          <p className="text-xl text-gray-400">Victor กำลังรอคำสั่งของคุณ...</p>
        </div>
      </div>
    );
  }

  return (
    <div className="glass rounded-3xl overflow-hidden border border-white/10">
      <div className="bg-black/40 px-6 py-3 text-sm flex items-center gap-2 border-b border-white/10">
        <div className="w-3 h-3 rounded-full bg-red-500"></div>
        <div className="w-3 h-3 rounded-full bg-yellow-500"></div>
        <div className="w-3 h-3 rounded-full bg-green-500"></div>
        <span className="ml-4 text-gray-400">Live Preview</span>
      </span>
      <div className="p-8 bg-white text-black min-h-[550px]" dangerouslySetInnerHTML={{ __html: code }} />
    </div>
  );
}