from src.ai.ai_client import call_ai


def explain_match(candidate, job, match_result):
    """
    AI explanation with rule-based fallback
    """

    input_text = f"""
Candidate:
{candidate.__dict__}

Job:
{job.__dict__}

Match Result:
{match_result}
"""

    ai_response = call_ai(
        system_prompt="Explain why the candidate matches or does not match the job.",
        user_input=input_text
    )

    # ✅ FALLBACK MODE
    if ai_response is None:
        return (
            f"Candidate scored {match_result['score']}%. "
            f"Matched skills: {match_result['matched_skills']}. "
            f"Missing skills: {match_result['missing_skills']}. "
            f"Recommendation based on rule-based analysis."
        )

    return ai_response
