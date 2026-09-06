import ollama

def judge_candidate(hire_result, reject_result):

    prompt = f"""
You are the final hiring manager.

Review both opinions.

HIRING ARGUMENTS:
{hire_result}

REJECTION ARGUMENTS:
{reject_result}

Provide:

1. Final Verdict
2. Confidence Score (0-100)
3. Short Explanation

Keep it concise.
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