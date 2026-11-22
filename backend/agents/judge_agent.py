import ollama

def judge_candidate(hire_result, reject_result):
    prompt = f"""You are the final hiring reviewer. Weigh the evidence fairly and return only:
VERDICT: Suitable / Partially Suitable / Not Suitable
CONFIDENCE: number from 0-100
REASON: one or two concise sentences
Do not invent candidate details.

SUPPORTING POINTS:
{hire_result}

GAPS:
{reject_result}
"""
    response = ollama.chat(model="gemma3:1b", messages=[{"role": "user", "content": prompt}], options={"num_predict": 100, "temperature": 0.2})
    return response["message"]["content"].strip()
