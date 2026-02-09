from src.utils.exceptions import ValidationError


def validate_candidate(candidate):
    """
    Validate mandatory fields in Candidate object
    """
    if not candidate.name:
        raise ValidationError("Candidate name missing")

    if not candidate.email:
        raise ValidationError("Candidate email missing")

    if not isinstance(candidate.skills, list):
        raise ValidationError("Skills must be a list")

    if candidate.experience < 0:
        raise ValidationError("Experience cannot be negative")

    return True
