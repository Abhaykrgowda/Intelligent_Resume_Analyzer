from src.storage.file_store import save_text


def export_text(report: str, filepath: str):
    """
    Save report as .txt file
    """
    save_text(report, filepath)
