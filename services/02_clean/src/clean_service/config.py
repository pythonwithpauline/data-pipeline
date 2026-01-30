from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class CleanConfig:
    lowercase_email: bool = True
    strip_whitespace: bool = True
