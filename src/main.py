from src.storage.file_store import read_text_file, read_json
from src.core.pipeline import run_pipeline
from src.utils.logger import logger

def main():
    resume_path = "data/incoming_resumes/resume_ai_test.txt"
    job_path = "data/job_profiles/python_developer.json"

    logger.info("Application started")

    resume_text = read_text_file(resume_path)
    job_data = read_json(job_path)

    run_pipeline(resume_text, job_data)

    logger.info("Application finished successfully")


if __name__ == "__main__":
    main()
