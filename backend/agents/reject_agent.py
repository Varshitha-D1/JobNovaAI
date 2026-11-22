import ollama

def reject_recommendation(resume_text, job_description):
    prompt = f"""Act as a recruiter. Give at most 3 concise bullet points describing important gaps between this resume and the job description. Mention missing skills or experience only when clearly relevant. Do not make assumptions or use an introduction.

RESUME:
{resume_text}

JOB DESCRIPTION:
{job_description}
"""
    response = ollama.chat(model="gemma3:1b", messages=[{"role": "user", "content": prompt}], options={"num_predict": 100, "temperature": 0.3})
    return response["message"]["content"].strip()
