import openai
import os
from dotenv import load_dotenv
from pathlib import Path
import logging

# Logging
logger = logging.getLogger(__name__)

# Load .env explicitly
ENV_PATH = Path(__file__).resolve().parents[2] / ".env"
load_dotenv(dotenv_path=ENV_PATH)

openai.api_key = os.getenv("OPENAI_API_KEY")


def call_ai(system_prompt: str, user_input: str) -> str | None:
    """
    Calls OpenAI API.
    Returns None if AI is unavailable (quota, network, auth, etc).
    NEVER raises OpenAI errors.
    """

    if not openai.api_key:
        logger.warning("OPENAI_API_KEY missing. Skipping AI call.")
        return None

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_input}
            ],
            temperature=0.2
        )

        return response.choices[0].message.content

    except Exception as e:
        # 🔑 THIS IS THE KEY LINE
        logger.warning(f"AI unavailable. Falling back. Reason: {e}")
        return None
