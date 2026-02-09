from src.models.candidate import Candidate
from src.parsing.field_extractors import (
    extract_name,
    extract_email,
    extract_skills,
    extract_experience,
    extract_education
)

from src.parsing.validation import validate_candidate
from src.parsing.confidence import calculate_confidence
from src.utils.exceptions import ParseError   # if utils exists



def parse_resume(text: str):
    """
    Parse raw resume text into structured candidate data
    """
    try:
        candidate = Candidate(
            name=extract_name(text),
            email=extract_email(text),
            skills=extract_skills(text),
            experience=extract_experience(text),
            education=extract_education(text)
        )

        validate_candidate(candidate)
        confidence = calculate_confidence(candidate)

        return {
            "candidate": candidate,
            "confidence": confidence
        }

    except Exception as e:
        raise ParseError(f"Resume parsing failed: {str(e)}")
