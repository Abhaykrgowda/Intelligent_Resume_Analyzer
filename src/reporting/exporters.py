from pathlib import Path
from datetime import datetime


def export_text(report: str, candidate_name: str):
    BASE_DIR = Path(__file__).resolve().parents[2]

    reports_dir = BASE_DIR / "data" / "processed" / "reports"
    reports_dir.mkdir(parents=True, exist_ok=True)

    safe_name = candidate_name.replace(" ", "_") if candidate_name else "candidate"

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = reports_dir / f"{safe_name}_{timestamp}.txt"

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(report)

    print(f"[REPORT SAVED] {file_path}")
