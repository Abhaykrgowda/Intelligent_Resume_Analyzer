import json
from pathlib import Path


def read_text_file(filepath: str) -> str:
    """
    Read a text file and return its content
    """
    return Path(filepath).read_text(encoding="utf-8")


def save_text(content: str, filepath: str):
    """
    Save plain text content to a file
    """
    path = Path(filepath)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def save_json(data: dict, filepath: str):
    """
    Save dictionary as formatted JSON
    """
    path = Path(filepath)
    path.parent.mkdir(parents=True, exist_ok=True)

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


def read_json(filepath: str) -> dict:
    """
    Read JSON file and return dictionary
    """
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)
