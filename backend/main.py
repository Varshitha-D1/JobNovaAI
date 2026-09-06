from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
import tempfile
from pydantic import BaseModel
from backend.agents.skill_gap import generate_skill_gap
from backend.agents.resume_parser import extract_resume_text
from backend.agents.summary_agent import generate_summary
from backend.agents.skill_gap import find_skill_gap
from backend.agents.interview_agent import generate_questions
from backend.agents.hire_agent import hire_recommendation
from backend.agents.reject_agent import reject_recommendation
from backend.agents.judge_agent import judge_candidate
from backend.agents.matcher import calculate_match_score

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {
        "message": "JobNova AI Backend Running"
    }


@app.post("/analyze_resume")
async def analyze_resume(
    file: UploadFile = File(...),
    job_description: str = Form(...)
):

    try:

        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".pdf"
        ) as temp_file:

            temp_file.write(
                await file.read()
            )

            temp_path = temp_file.name

        resume_text = extract_resume_text(temp_path)

        summary = generate_summary(
            resume_text
        )

        skill_gap = find_skill_gap(
            resume_text,
            job_description
        )

        questions = generate_questions(
            resume_text,
            job_description
        )

        hire_result = hire_recommendation(
            resume_text,
            job_description
        )

        reject_result = reject_recommendation(
            resume_text,
            job_description
        )

        judge_result = judge_candidate(
            hire_result,
            reject_result
        )

        return {
            "status": "success",
            "summary": summary,
            "skill_gap": skill_gap,
            "questions": questions,
            "hire": hire_result,
            "reject": reject_result,
            "judge": judge_result
        }

    except Exception as e:

        return {
            "status": "error",
            "message": str(e)
        }

class SkillRequest(BaseModel):
    career_goal: str


@app.post("/skill_navigator")
def skill_navigator(
    request: SkillRequest
):

    roadmap = generate_skill_gap(
        request.career_goal
    )

    return {
        "roadmap": roadmap
    }

@app.post("/company_match")
async def company_match(
    file: UploadFile = File(...),
    job_description: str = Form(...)
):

    try:

        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".pdf"
        ) as temp_file:

            temp_file.write(
                await file.read()
            )

            temp_path = temp_file.name

        resume_text = extract_resume_text(
            temp_path
        )

        result = calculate_match_score(
            resume_text,
            job_description
        )

        return {
            "status": "success",
            "score": result["score"],
            "reason": result["reason"]
        }

    except Exception as e:

        return {
            "status": "error",
            "message": str(e)
        }