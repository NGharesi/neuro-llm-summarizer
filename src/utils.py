from datetime import datetime
from pathlib import Path

import pandas as pd


def load_sample_text(file_path: Path) -> str:
    if not file_path.exists():
        return ""
    return file_path.read_text(encoding="utf-8")


def ensure_output_directory(output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)


def save_summary_to_csv(summary, paper_text: str, model_name: str, output_path: Path) -> Path:
    ensure_output_directory(output_path)

    row = pd.DataFrame(
        [
            {
                "created_at": datetime.now().isoformat(timespec="seconds"),
                "model": model_name,
                "paper_text_preview": paper_text[:120].replace("\n", " "),
                "research_question": summary.research_question,
                "methods": summary.methods,
                "participants_or_data": summary.participants_or_data,
                "main_findings": summary.main_findings,
                "limitations": summary.limitations,
                "misunderstood_terms": "; ".join(summary.misunderstood_terms),
                "confidence_score": summary.confidence_score,
            }
        ]
    )

    if output_path.exists():
        existing = pd.read_csv(output_path)
        row = pd.concat([existing, row], ignore_index=True)

    row.to_csv(output_path, index=False)
    return output_path


def read_saved_summaries(output_path: Path) -> pd.DataFrame:
    if not output_path.exists():
        return pd.DataFrame()
    return pd.read_csv(output_path)
