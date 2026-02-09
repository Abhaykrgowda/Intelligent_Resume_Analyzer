from config.prompts import PROMPTS
from ai.ai_client import call_ai


def generate_interview_questions(candidate):
    return call_ai(PROMPTS["recommendation"], str(candidate.__dict__))
