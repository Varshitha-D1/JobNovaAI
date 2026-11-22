import ollama


def generate_summary(resume_text):
    prompt = f"""You are an expert recruiter. Summarize the candidate's resume in 4-5 concise bullet points. Cover education, strongest skills, relevant projects/experience, and overall profile. Use only facts present in the resume. Avoid introductions, repetition, and generic advice.

RESUME:
{resume_text}
"""
    response = ollama.chat(
        model="gemma3:1b",
        messages=[{"role": "user", "content": prompt}],
        options={"num_predict": 320, "temperature": 0.3},
    )
    return response["message"]["content"].strip()