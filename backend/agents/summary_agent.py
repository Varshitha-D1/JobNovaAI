import ollama

def generate_summary(resume_text):

    prompt = f"""
You are an expert recruiter.

Summarize this resume in 5-6 lines.

Focus on:
- Education
- Skills
- Projects
- Experience
- Overall profile

Resume:
{resume_text}
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