def build_report(candidate, job, match_result, ai_explanation):
    """
    Build a human-readable candidate analysis report
    """

    score = match_result["score"]
    matched = match_result["matched_skills"]
    missing = match_result["missing_skills"]

    if score >= 80:
        recommendation = "✅ STRONGLY RECOMMENDED"
    elif score >= 60:
        recommendation = "✓ RECOMMENDED"
    elif score >= 40:
        recommendation = "⚠ MAYBE"
    else:
        recommendation = "✗ NOT RECOMMENDED"

    report = f"""
==================================================
            CANDIDATE ANALYSIS REPORT
==================================================

Candidate Name : {candidate.name}
Email          : {candidate.email}
Job Role       : {job.title}
Match Score    : {score}/100

------------------ SKILLS -------------------------
Matched Skills :
{', '.join(matched) if matched else 'None'}

Missing Skills :
{', '.join(missing) if missing else 'None'}

---------------- AI EXPLANATION -------------------
{ai_explanation}

---------------- RECOMMENDATION ------------------
{recommendation}

==================================================
"""
    return report
