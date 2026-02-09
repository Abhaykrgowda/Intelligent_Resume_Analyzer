import os
from dotenv import load_dotenv
from pathlib import Path
import logging
from groq import Groq

logger = logging.getLogger(__name__)

# Load .env
ENV_PATH = Path(__file__).resolve().parents[2] / ".env"
load_dotenv(dotenv_path=ENV_PATH)

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def call_ai(system_prompt: str, user_input: str) -> str | None:
    """
    Groq-based LLM call.
    Returns None if AI is unavailable.
    """

    if not os.getenv("GROQ_API_KEY"):
        logger.warning("GROQ_API_KEY missing. Skipping AI.")
        return None

    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant"
,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_input}
            ],
            temperature=0.2
        )

        return response.choices[0].message.content

    except Exception as e:
        logger.warning(f"Groq unavailable. Falling back. Reason: {e}")
        return None
