from agents.resume_parser import extract_resume_text
from agents.matcher import calculate_match_score

def rank_candidates(uploaded_files, job_description):

    candidates = []

    for file in uploaded_files:

        resume_text = extract_resume_text(file)

        result = calculate_match_score(
            resume_text,
            job_description
        )

        candidates.append({
            "name": file.name,
            "score": result["score"],
            "reason": result["reason"],
            "resume_text": resume_text
        })

    candidates.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return candidates