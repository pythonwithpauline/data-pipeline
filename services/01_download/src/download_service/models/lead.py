from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Lead:
    id: int
    name: str
    email: str
    company: str
