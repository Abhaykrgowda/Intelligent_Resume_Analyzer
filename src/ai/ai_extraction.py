import json
import re
from src.ai.ai_client import call_ai
from src.models.candidate import Candidate


def normalize_experience(exp):
    """
    Normalize AI-produced experience into integer years.
    Handles int, string, dict, or None.
    """
    if exp is None:
        return 0

    if isinstance(exp, int):
        return exp

    if isinstance(exp, str):
        # Examples: "4 years", "around 3 yrs"
        digits = "".join(ch for ch in exp if ch.isdigit())
        return int(digits) if digits else 0

    if isinstance(exp, dict):
        # Example: {"years": 4}
        if "years" in exp and isinstance(exp["years"], int):
            return exp["years"]

    return 0


def extract_json_from_text(text: str) -> dict | None:
    """
    Extract the first valid JSON object from AI response text.
    """
    try:
        match = re.search(r"\{.*\}", text, re.DOTALL)
        if not match:
            return None
        return json.loads(match.group())
    except Exception:
        return None


def ai_extract_resume(resume_text: str) -> Candidate | None:
    """
    Uses AI to extract structured resume data.
    Returns Candidate on success, None on failure.
    NEVER raises due to AI errors.
    """

    response = call_ai(
        system_prompt="Extract resume data into strict JSON.",
        user_input=resume_text
    )

    # AI unavailable
    if response is None:
        return None

    data = extract_json_from_text(response)
    if data is None:
        return None

    return Candidate(
        name=data.get("name"),
        email=data.get("email"),
        skills=data.get("skills", []) if isinstance(data.get("skills"), list) else [],
        experience=normalize_experience(data.get("experience")),
        education=data.get("education")
    )
