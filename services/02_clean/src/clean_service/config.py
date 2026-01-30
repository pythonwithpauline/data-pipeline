from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict


@dataclass(frozen=True)
class CleaningConfig:
    trim_whitespace: bool = True
    lowercase_email: bool = True


@dataclass(frozen=True)
class CleanConfig:
    input_path: str
    output_path: str
    cleaning: CleaningConfig

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "CleanConfig":
        cleaning_d = d.get("cleaning", {}) or {}
        return CleanConfig(
            input_path=str(d["input_path"]),
            output_path=str(d["output_path"]),
            cleaning=CleaningConfig(
                trim_whitespace=bool(cleaning_d.get("trim_whitespace", True)),
                lowercase_email=bool(cleaning_d.get("lowercase_email", True)),
            ),
        )
