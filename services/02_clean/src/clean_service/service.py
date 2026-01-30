from __future__ import annotations

from pathlib import Path

import pandas as pd

from .config import CleanConfig


def run(config: CleanConfig) -> Path:
    in_path = Path(config.input_path)
    if not in_path.exists():
        raise FileNotFoundError(f"Input file not found: {in_path}")

    df = pd.read_excel(in_path)

    if config.cleaning.trim_whitespace:
        for col in ["name", "email", "company"]:
            if col in df.columns:
                df[col] = df[col].astype(str).str.strip()

    if config.cleaning.lowercase_email and "email" in df.columns:
        df["email"] = df["email"].astype(str).str.lower()

    out_path = Path(config.output_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_excel(out_path, index=False)
    return out_path
