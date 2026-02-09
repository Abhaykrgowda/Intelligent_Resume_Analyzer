from src.parsing.resume_parser import parse_resume
from src.ai.ai_extraction import ai_extract_resume
from src.ai.ai_reasoning import explain_match
from src.utils.exceptions import ParseError
from src.matching.matcher import match_candidate
from src.reporting.report_builder import build_report
from src.reporting.exporters import export_text
from src.models.job import Job
from src.models.candidate import Candidate
from src.utils.logger import logger


def run_pipeline(resume_text: str, job_data: dict):
    logger.info("Pipeline started")

    # Build Job object
    job = Job.from_dict(job_data)

    # -------------------------------
    # 1️⃣ RULE-BASED PARSING
    # -------------------------------
    try:
        parse_result = parse_resume(resume_text)
        candidate = parse_result["candidate"]
        logger.info("Rule-based parsing successful")

    # -------------------------------
    # 2️⃣ AI FALLBACK
    # -------------------------------
    except ParseError as e:
        logger.warning(
            f"Rule-based parsing failed. Falling back to AI. Reason: {e}"
        )
        candidate = ai_extract_resume(resume_text)

        # -------------------------------
        # 3️⃣ FINAL SAFE FALLBACK
        # -------------------------------
        if candidate is None:
            logger.warning(
                "AI extraction failed. Using minimal fallback candidate."
            )

            candidate = Candidate(
                name="Unknown Candidate",
                email=None,
                skills=[],
                experience=0,
                education=None
            )

    # -------------------------------
    # 4️⃣ MATCHING
    # -------------------------------
    match_result = match_candidate(candidate, job)

    # -------------------------------
    # 5️⃣ AI / RULE-BASED EXPLANATION
    # -------------------------------
    ai_explanation = explain_match(candidate, job, match_result)

    # -------------------------------
    # 6️⃣ REPORT GENERATION
    # -------------------------------
    report = build_report(candidate, job, match_result, ai_explanation)
    export_text(report, candidate.name)

    logger.info("Pipeline completed successfully")
