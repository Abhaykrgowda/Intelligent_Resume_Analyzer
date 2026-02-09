from fuzzywuzzy import fuzz


def fuzzy_skill_match(candidate_skill, required_skill, threshold=85):
    """
    Returns True if skills are similar above threshold
    """
    score = fuzz.ratio(candidate_skill.lower(), required_skill.lower())
    return score >= threshold
