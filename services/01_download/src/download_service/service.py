from __future__ import annotations

import json
from pathlib import Path

from .config import DownloadConfig
from .models.lead import Lead


def run(config: DownloadConfig, out_path: str) -> Path:
    """Generate a few dummy leads and write them as JSONL."""
    out = Path(out_path)
    out.parent.mkdir(parents=True, exist_ok=True)

    leads = [
        Lead(id=i, name=f"Lead {i}", email=f"lead{i}@example.com", company="Acme")
        for i in range(1, config.n_leads + 1)
    ]

    with out.open("w", encoding="utf-8") as f:
        for lead in leads:
            f.write(json.dumps(lead.__dict__, ensure_ascii=False) + "\n")

    return out
