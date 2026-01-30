from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class DownloadConfig:
    # Dummy params – imagine these come from client configs later
    n_leads: int = 5
    source_name: str = "dummy"
