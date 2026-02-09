import json
from pathlib import Path

from src.ai.ai_client import call_ai
from src.models.candidate import Candidate
from src.utils.exceptions import ParseError


# Resolve path relative to this file:
# ai_extraction.py → src/ai/ → src/config/prompts.json
SRC_DIR = Path(__file__).resolve().parents[1]   # points to src/
PROMPTS_PATH = SRC_DIR / "config" / "prompts.json"

PROMPTS = json.loads(PROMPTS_PATH.read_text(encoding="utf-8"))


def ai_extract_resume(resume_text: str) -> Candidate:
    """
    Uses LLM to extract structured resume data when rule-based parsing is insufficient
    """
    try:
        response = call_ai(
            system_prompt=PROMPTS["extraction"],
            user_input=resume_text
        )

        # AI is instructed to return STRICT JSON
        data = json.loads(response)

        return Candidate(
            name=data.get("name"),
            email=data.get("email"),
            skills=data.get("skills", []),
            experience=data.get("experience", 0),
            education=data.get("education")
        )

    except json.JSONDecodeError:
        raise ParseError("AI extraction failed: Invalid JSON format")

    except Exception as e:
        raise ParseError(f"AI extraction failed: {str(e)}")
