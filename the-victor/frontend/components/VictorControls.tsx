'use client';

export default function VictorControls({ projectName, setProjectName }: any) {
  return (
    <div className="flex items-center gap-4">
      <input
        value={projectName}
        onChange={(e) => setProjectName(e.target.value)}
        className="bg-white/5 border border-white/10 rounded-xl px-4 py-2 text-sm focus:outline-none w-64"
      />
      <button className="px-5 py-2 rounded-xl bg-white/10 hover:bg-white/20 text-sm">God Mode</button>
      <button className="px-5 py-2 rounded-xl bg-emerald-600 hover:bg-emerald-700 text-sm">Deploy</button>
    </div>
  );
}