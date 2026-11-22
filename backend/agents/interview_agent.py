import ollama


def generate_questions(resume_text, job_description):
    prompt = f"""Act as a technical interviewer. Create exactly 5 clear, personalized interview questions based on the candidate's resume and the job description. Focus on relevant skills, projects, and role requirements. Output only a numbered list of questions; no introduction, answers, or explanations.

RESUME:
{resume_text}

JOB DESCRIPTION:
{job_description}
"""
    response = ollama.chat(
        model="gemma3:1b",
        messages=[{"role": "user", "content": prompt}],
        options={"num_predict": 350, "temperature": 0.4},
    )
    return response["message"]["content"].strip()