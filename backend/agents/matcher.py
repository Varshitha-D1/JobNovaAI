import ollama
import json
import re

def calculate_match_score(
    resume_text,
    job_description
):

    prompt = f"""
You are an expert recruiter.

Compare the resume and job description.

Return ONLY valid JSON.

Example:

{{
    "score": 85,
    "reason": "Strong match in Python, Machine Learning and SQL."
}}

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

    output = response["message"]["content"]

    print("\nMATCHER OUTPUT:\n")
    print(output)

    try:

        json_match = re.search(
            r'\{.*?\}',
            output,
            re.DOTALL
        )

        if json_match:

            result = json.loads(
                json_match.group()
            )

            score = result.get(
                "score",
                50
            )

            reason = result.get(
                "reason",
                "Match calculated successfully."
            )

            return {
                "score": score,
                "reason": reason
            }

    except Exception as e:

        print(e)

    return {
        "score": 50,
        "reason": "AI could not generate proper output."
    }