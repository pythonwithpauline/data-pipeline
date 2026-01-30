from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict


@dataclass(frozen=True)
class HttpConfig:
    base_url: str
    timeout_seconds: int = 10


@dataclass(frozen=True)
class LeadDefaults:
    company: str = "Unknown"


@dataclass(frozen=True)
class DownloadConfig:
    output_path: str
    http: HttpConfig
    lead_defaults: LeadDefaults

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "DownloadConfig":
        http_d = d.get("http", {}) or {}
        defaults_d = d.get("lead_defaults", {}) or {}

        return DownloadConfig(
            output_path=str(d["output_path"]),
            http=HttpConfig(
                base_url=str(http_d.get("base_url", "")),
                timeout_seconds=int(http_d.get("timeout_seconds", 10)),
            ),
            lead_defaults=LeadDefaults(
                company=str(defaults_d.get("company", "Unknown")),
            ),
        )
