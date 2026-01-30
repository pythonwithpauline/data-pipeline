from __future__ import annotations

from pathlib import Path
from typing import List

import pandas as pd

from .adapters.http_client import DummyHttpClient
from .config import DownloadConfig
from .models.lead import Lead


def run(config: DownloadConfig) -> Path:
    """Fetch leads from the HTTP boundary and write them to an Excel file."""
    client = DummyHttpClient()
    leads: List[Lead] = client.fetch_leads(config)

    out_path = Path(config.output_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    df = pd.DataFrame(
        [
            {"id": l.id, "name": l.name, "email": l.email, "company": l.company}
            for l in leads
        ]
    )
    df.to_excel(out_path, index=False)
    return out_path
