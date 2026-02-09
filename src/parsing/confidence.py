def calculate_confidence(candidate):
    """
    Calculate confidence score (0–100) for parsed resume
    """
    score = 0

    if candidate.name:
        score += 20
    if candidate.email:
        score += 20
    if candidate.skills and len(candidate.skills) >= 3:
        score += 30
    if candidate.experience > 0:
        score += 20
    if candidate.education:
        score += 10

    return score
