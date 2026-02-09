import re

COMMON_SKILLS = [
    "python", "java", "c++", "sql",
    "machine learning", "deep learning",
    "data science", "flask", "django",
    "git", "aws", "docker", "kubernetes"
]


def extract_name(text: str):
    """
    Extract candidate name from the top lines of resume
    """
    lines = text.strip().split("\n")
    for line in lines[:5]:
        words = line.strip().split()
        if 1 < len(words) <= 4 and line.replace(" ", "").isalpha():
            return line.strip()
    return None


def extract_email(text: str):
    """
    Extract email using regex
    """
    pattern = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"
    match = re.search(pattern, text)
    return match.group() if match else None


def extract_experience(text: str):
    """
    Extract years of experience
    """
    match = re.search(r"(\d+)\+?\s*(years|yrs)", text.lower())
    return int(match.group(1)) if match else 0


def extract_skills(text: str):
    """
    Extract skills by keyword matching
    """
    text_lower = text.lower()
    found_skills = [skill for skill in COMMON_SKILLS if skill in text_lower]
    return list(set(found_skills))


def extract_education(text: str):
    """
    Extract highest education level
    """
    education_keywords = [
        "bachelor", "master", "phd",
        "b.tech", "m.tech", "b.e", "mca"
    ]

    text_lower = text.lower()
    for edu in education_keywords:
        if edu in text_lower:
            return edu.upper()

    return None
