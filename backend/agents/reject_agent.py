import ollama

def reject_recommendation(resume_text, job_description):

    prompt = f"""
You are a strict recruiter.

Analyze the candidate.

Give reasons why this candidate SHOULD NOT be hired.

Focus on:
- Missing skills
- Missing experience
- Potential concerns

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