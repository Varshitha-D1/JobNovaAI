import ollama

def hire_recommendation(resume_text, job_description):

    prompt = f"""
You are a senior recruiter.

Analyze the candidate.

Give reasons why this candidate SHOULD be hired.

Return only bullet points.

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