import ollama

def generate_questions(resume_text, job_description):

    prompt = f"""
You are a technical interviewer.

Based on the candidate resume and job description,
generate 5 personalized technical interview questions.

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