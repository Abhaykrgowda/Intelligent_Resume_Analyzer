from src.matching.scoring_strategies import BasicScoring


def match_candidate(candidate, job, strategy=None):
    """
    Match candidate against job using selected strategy
    """
    strategy = strategy or BasicScoring()
    score = strategy.calculate(candidate, job)

    matched_skills = list(set(candidate.skills) & set(job.required_skills))
    missing_skills = list(set(job.required_skills) - set(candidate.skills))

    return {
        "score": score,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills
    }
