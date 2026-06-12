import { NextRequest, NextResponse } from 'next/server';
import { victor } from '@/../../backend/core/victor_core';

export async function POST(request: NextRequest) {
  try {
    const body = await request.json();
    const { prompt, project_name = "Untitled Project" } = body;

    if (!prompt) {
      return NextResponse.json({ error: "กรุณาใส่ prompt" }, { status: 400 });
    }

    const result = await victor.build_website(prompt, project_name);

    return NextResponse.json({
      success: true,
      ...result
    });

  } catch (error) {
    console.error("Victor Build Error:", error);
    return NextResponse.json({ 
      success: false, 
      error: "Victor เกิดข้อผิดพลาดในการสร้างเว็บ" 
    }, { status: 500 });
  }
}
