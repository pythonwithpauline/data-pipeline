from __future__ import annotations

from typing import List

from ..config import DownloadConfig
from ..models.lead import Lead


class DummyHttpClient:
    """Fake HTTP client that returns domain objects (Lead)."""

    def fetch_leads(self, config: DownloadConfig) -> List[Lead]:
        company = config.lead_defaults.company

        raw = [
            {"id": 1, "name": " Alice  ", "email": "ALICE@EXAMPLE.COM", "company": company},
            {"id": 2, "name": "Bob", "email": "bob@example.com ", "company": company},
            {"id": 3, "name": "Chloé", "email": "chloe@example.com", "company": company},
        ]

        leads: List[Lead] = []
        for item in raw:
            leads.append(
                Lead(
                    id=int(item["id"]),
                    name=str(item["name"]),
                    email=str(item["email"]),
                    company=str(item["company"]),
                )
            )
        return leads
