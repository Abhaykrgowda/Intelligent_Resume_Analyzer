# Intelligent Resume Analyzer

Analyze a resume against a job profile, score the match, and generate a plain-text report. The pipeline blends rule-based parsing with optional LLM extraction and explanation.

## Features
- Rule-based resume parsing with confidence scoring.
- AI fallback extraction when parsing confidence is low.
- Skill matching with fuzzy logic and configurable thresholds.
- AI-generated match explanation (optional).
- Text report export to `data/processed/reports/`.

## How It Works
1. Parse resume text into a candidate profile.
2. If parsing confidence is below the threshold, use AI to extract the profile.
3. Load job profile and compute match score + skill gaps.
4. Generate an AI explanation for the match.
5. Build and export a report.

## Requirements
- Python 3.10+ recommended
- Packages in `requirements.txt`

## Setup
1. Create and activate a virtual environment.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_api_key_here
```

AI features are optional. If the key is missing or the API is unavailable, the pipeline continues without AI outputs.

## Run
From the project root:

```bash
python -m src.main
```

The default inputs are:
- Resume: `data/incoming_resumes/resume_ai_test.txt`
- Job profile: `data/job_profiles/python_developer.json`

The report is saved to:
- `data/processed/reports/<Candidate_Name>.txt`

## Configure Inputs
Edit the paths in `src/main.py`:
- `resume_path`
- `job_path`

## Configuration
- Thresholds and limits: `src/config/settings.json`
- AI prompts: `src/config/prompts.json`

## Output Format
Reports include:
- Candidate and job summary
- Match score
- Matched and missing skills
- AI explanation
- Recommendation label

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
- If AI output is empty, check that `OPENAI_API_KEY` is set.
- If imports fail, ensure you are running from the project root with `python -m src.main`.
