import ollama

def hire_recommendation(resume_text, job_description):
    prompt = f"""Act as a recruiter. Give at most 3 concise bullet points explaining why this candidate may be suitable for the role. Use evidence from the resume and job description only. No introduction.

RESUME:
{resume_text}

JOB DESCRIPTION:
{job_description}
"""
    response = ollama.chat(model="gemma3:1b", messages=[{"role": "user", "content": prompt}], options={"num_predict": 100, "temperature": 0.3})
    return response["message"]["content"].strip()
