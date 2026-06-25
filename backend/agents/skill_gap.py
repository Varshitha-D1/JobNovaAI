import ollama


def find_skill_gap(
    resume_text,
    job_description
):

    prompt = f"""
You are an expert AI recruiter.

Compare the candidate resume and job description.

Extract only meaningful technical skills.

Return in this format:

FOUND SKILLS:
- skill1
- skill2

MISSING SKILLS:
- skill3
- skill4

Resume:
{resume_text}

Job Description:
{job_description}
"""

    response = ollama.chat(
        model="gemma3:1b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]


def generate_skill_gap(
    career_goal
):

    prompt = f"""
You are an AI Career Mentor.

The user wants to become:

{career_goal}

IMPORTANT:
Generate roadmap ONLY for {career_goal}.
Do not generate roadmap for any other career.

Return in this format:

REQUIRED SKILLS:
- skill1
- skill2

LEARNING PATH:
1. Step One
2. Step Two

TOOLS:
- tool1
- tool2

PROJECTS:
- project1
- project2

CAREER TIPS:
- tip1
- tip2
"""

    response = ollama.chat(
        model="gemma3:1b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]