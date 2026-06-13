'use client';

import { useState } from 'react';

interface Project {
  id: string;
  name: string;
  prompt: string;
  createdAt: string;
}

export default function ProjectManager() {
  const [projects, setProjects] = useState<Project[]>([
    {
      id: '1',
      name: 'เว็บขายคอร์สออนไลน์',
      prompt: 'สร้างเว็บขายคอร์สออนไลน์พรีเมี่ยม',
      createdAt: new Date().toISOString()
    }
  ]);
  const [showList, setShowList] = useState(false);

  const saveCurrentProject = () => {
    const newProject: Project = {
      id: Date.now().toString(),
      name: `Project ${projects.length + 1}`,
      prompt: 'สร้างเว็บจาก Victor',
      createdAt: new Date().toISOString()
    };
    setProjects([newProject, ...projects]);
    alert('บันทึกโปรเจกต์เรียบร้อยแล้ว!');
  };

  return (
    <div className="relative">
      <button
        onClick={() => setShowList(!showList)}
        className="px-4 py-2 bg-white/10 hover:bg-white/20 rounded-2xl text-sm border border-white/10 flex items-center gap-2"
      >
        📁 โปรเจกต์ของฉัน ({projects.length})
      </button>

      {showList && (
        <div className="absolute right-0 mt-2 w-80 glass rounded-3xl p-4 border border-white/10 z-50">
          <div className="flex justify-between items-center mb-4">
            <h3 className="font-semibold">โปรเจกต์ที่บันทึกไว้</h3>
            <button 
              onClick={saveCurrentProject}
              className="text-xs px-3 py-1 bg-purple-600 rounded-xl hover:bg-purple-700"
            >
              + บันทึกปัจจุบัน
            </button>
          </div>

          <div className="space-y-2 max-h-80 overflow-auto">
            {projects.length === 0 ? (
              <p className="text-gray-400 text-sm text-center py-4">ยังไม่มีโปรเจกต์</p>
            ) : (
              projects.map((project) => (
                <div 
                  key={project.id}
                  className="p-3 bg-white/5 rounded-2xl hover:bg-white/10 cursor-pointer border border-white/5"
                >
                  <div className="font-medium text-sm">{project.name}</div>
                  <div className="text-xs text-gray-400 mt-1 line-clamp-2">{project.prompt}</div>
                  <div className="text-[10px] text-gray-500 mt-2">
                    {new Date(project.createdAt).toLocaleDateString('th-TH')}
                  </div>
                </div>
              ))
            )}
          </div>
        </div>
      )}
    </div>
  );
}
