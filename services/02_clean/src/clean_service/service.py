from __future__ import annotations

import json
from pathlib import Path

from .config import CleanConfig
from .transforms.clean import clean_record


def run(config: CleanConfig, in_path: str, out_path: str) -> Path:
    inp = Path(in_path)
    out = Path(out_path)
    out.parent.mkdir(parents=True, exist_ok=True)

    with inp.open("r", encoding="utf-8") as f_in, out.open("w", encoding="utf-8") as f_out:
        for line in f_in:
            if not line.strip():
                continue
            rec = json.loads(line)
            cleaned = clean_record(
                rec,
                lowercase_email=config.lowercase_email,
                strip_whitespace=config.strip_whitespace,
            )
            f_out.write(json.dumps(cleaned, ensure_ascii=False) + "\n")

    return out
