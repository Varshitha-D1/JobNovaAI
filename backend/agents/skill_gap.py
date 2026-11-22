import ollama


def find_skill_gap(resume_text, job_description):
    prompt = f"""Compare the resume with the job description. List only relevant technical skills, using concise bullets and no explanations. Use this exact format:
FOUND SKILLS (max 6):
- ...
MISSING OR WEAK SKILLS (max 5):
- ...
Do not invent skills or experience.

RESUME:
{resume_text}

JOB DESCRIPTION:
{job_description}
"""
    response = ollama.chat(
        model="gemma3:1b",
        messages=[{"role": "user", "content": prompt}],
        options={"num_predict": 250, "temperature": 0.3},
    )
    return response["message"]["content"].strip()


def generate_skill_gap(career_goal):
    prompt = f"""You are a concise career mentor. Create a complete, practical roadmap for: {career_goal}. Finish every section completely without cutting off. Use these exact headings and short bullets:
REQUIRED SKILLS (max 5)
LEARNING PATH (4 ordered steps)
TOOLS (max 4)
BEGINNER PROJECTS (2 ideas)
CAREER TIP (1 sentence)
Avoid long explanations and generic introductions.
"""
    response = ollama.chat(
        model="gemma3:1b",
        messages=[{"role": "user", "content": prompt}],
        options={"num_predict": 500, "temperature": 0.4},
    )
    return response["message"]["content"].strip()