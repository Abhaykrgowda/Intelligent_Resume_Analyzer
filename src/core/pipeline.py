from src.parsing.resume_parser import parse_resume
from src.ai.ai_extraction import ai_extract_resume
from src.ai.ai_reasoning import explain_match
from src.matching.matcher import match_candidate
from src.reporting.report_builder import build_report
from src.reporting.exporters import export_text
from src.models.job import Job
from src.utils.logger import logger



CONFIDENCE_THRESHOLD = 70


def run_pipeline(resume_text: str, job_data: dict):
    logger.info("Pipeline started")

    # STEP 1: Rule-based parsing
    parse_result = parse_resume(resume_text)
    confidence = parse_result["confidence"]

    if confidence < CONFIDENCE_THRESHOLD:
        logger.info("Low confidence parsing, using AI extraction")
        candidate = ai_extract_resume(resume_text)
    else:
        candidate = parse_result["candidate"]

    # STEP 2: Job object
    job = Job(
        title=job_data["title"],
        required_skills=job_data["required_skills"],
        min_experience=job_data["min_experience"],
        education=job_data["education"]
    )

    # STEP 3: Matching
    match_result = match_candidate(candidate, job)

    # STEP 4: AI explanation
    ai_explanation = explain_match(candidate, job, match_result)

    # STEP 5: Reporting
    report = build_report(candidate, job, match_result, ai_explanation)

    # STEP 6: Save report
    filename = f"data/processed/reports/{candidate.name.replace(' ', '_')}.txt"
    export_text(report, filename)

    logger.info("Pipeline completed successfully")
