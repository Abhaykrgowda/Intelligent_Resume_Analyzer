# Intelligent Resume Analyzer

Analyze resumes against job profiles, score the match, and export a clear, plain-text report. The pipeline combines deterministic parsing with optional LLM extraction and explanation.

## Highlights
- Rule-based parsing with confidence scoring
- AI fallback extraction for low-confidence parses
- Fuzzy skill matching with configurable thresholds
- Optional AI match explanation
- Text report export to `data/processed/reports/`

## Quick Start
1. Create and activate a virtual environment.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. (Optional) Create a `.env` file in the project root (Grok/xAI):

```env
GROK_API_KEY=your_api_key_here
```

4. Run the pipeline:

```bash
python -m src.main
```

AI features are optional. If the Grok API key is missing or the service is unavailable, the pipeline continues without AI outputs.

## Default Inputs
- Resume: `data/incoming_resumes/resume_ai_test.txt`
- Job profile: `data/job_profiles/python_developer.json`

## Output
Reports are saved to:
- `data/processed/reports/<Candidate_Name>.txt`

Each report includes:
- Candidate and job summary
- Match score
- Matched and missing skills
- AI explanation (when available)
- Recommendation label

## How It Works
1. Parse resume text into a candidate profile.
2. If confidence is below the threshold, use AI to extract the profile.
3. Load the job profile and compute match score and skill gaps.
4. Generate an AI explanation for the match (optional).
5. Build and export the report.

## Configuration
- Runtime thresholds and limits: `src/config/settings.json`
- AI prompts: `src/config/prompts.json`
- Input paths: update `resume_path` and `job_path` in `src/main.py`

## Requirements
- Python 3.10+ recommended
- Packages listed in `requirements.txt`

## Project Layout
```
src/
  ai/                # LLM calls and reasoning
  config/            # Settings and prompts
  core/              # Pipeline orchestration
  matching/          # Matching logic and scoring
  models/            # Candidate and job models
  parsing/           # Resume parsing and validation
  reporting/         # Report building and exporting
  storage/           # File IO utilities
  utils/             # Logging and exceptions

data/
  incoming_resumes/  # Raw resumes
  job_profiles/      # Job definitions
  processed/reports/ # Generated reports
```

## Troubleshooting
- If AI output is empty, confirm `GROK_API_KEY` is set.
- If imports fail, run from the project root with `python -m src.main`.
