import asyncio
import os
import tempfile

from fastapi import FastAPI, File, Form, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from backend.agents.hire_agent import hire_recommendation
from backend.agents.interview_agent import generate_questions
from backend.agents.judge_agent import judge_candidate
from backend.agents.matcher import calculate_match_score
from backend.agents.reject_agent import reject_recommendation
from backend.agents.resume_parser import extract_resume_text
from backend.agents.skill_gap import find_skill_gap, generate_skill_gap
from backend.agents.summary_agent import generate_summary

app = FastAPI(title="JobNova AI Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


class SkillRequest(BaseModel):
    career_goal: str


async def save_and_extract_pdf(file: UploadFile) -> str:
    filename = file.filename or ""
    if not filename.lower().endswith(".pdf"):
        raise ValueError("Please upload a valid PDF file.")

    content = await file.read()
    if not content:
        raise ValueError("The uploaded PDF file is empty.")

    temp_path = None
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
            temp_file.write(content)
            temp_path = temp_file.name

        resume_text = await asyncio.to_thread(extract_resume_text, temp_path)
    finally:
        if temp_path and os.path.exists(temp_path):
            os.remove(temp_path)

    if not resume_text.strip():
        raise ValueError(
            "No readable text found in this PDF. Please upload a text-based PDF rather than a scanned image."
        )

    return resume_text


@app.get("/")
def home():
    return {"message": "JobNova AI Backend Running"}


@app.post("/analyze_resume")
async def analyze_resume(
    file: UploadFile = File(...),
    job_description: str = Form(...),
):
    try:
        resume_text = await save_and_extract_pdf(file)

        summary = await asyncio.to_thread(generate_summary, resume_text)
        skill_gap = await asyncio.to_thread(
            find_skill_gap, resume_text, job_description
        )
        questions = await asyncio.to_thread(
            generate_questions, resume_text, job_description
        )
        hire_result = await asyncio.to_thread(
            hire_recommendation, resume_text, job_description
        )
        reject_result = await asyncio.to_thread(
            reject_recommendation, resume_text, job_description
        )
        judge_result = await asyncio.to_thread(
            judge_candidate, hire_result, reject_result
        )

        return {
            "status": "success",
            "summary": summary,
            "skill_gap": skill_gap,
            "questions": questions,
            "hire": hire_result,
            "reject": reject_result,
            "judge": judge_result,
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}


@app.post("/generate_questions")
async def interview_questions(
    file: UploadFile = File(...),
    job_description: str = Form(...),
):
    try:
        resume_text = await save_and_extract_pdf(file)
        questions = await asyncio.to_thread(
            generate_questions, resume_text, job_description
        )
        return {
            "status": "success",
            "questions": questions,
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}


@app.post("/skill_navigator")
async def skill_navigator(request: SkillRequest):
    try:
        career_goal = request.career_goal.strip()
        if not career_goal:
            return {"status": "error", "message": "Please select a career goal."}

        roadmap = await asyncio.to_thread(generate_skill_gap, career_goal)
        return {
            "status": "success",
            "roadmap": roadmap,
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}


@app.post("/company_match")
async def company_match(
    file: UploadFile = File(...),
    job_description: str = Form(...),
):
    try:
        resume_text = await save_and_extract_pdf(file)
        result = await asyncio.to_thread(
            calculate_match_score, resume_text, job_description
        )
        return {
            "status": "success",
            "score": result["score"],
            "reason": result["reason"],
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}