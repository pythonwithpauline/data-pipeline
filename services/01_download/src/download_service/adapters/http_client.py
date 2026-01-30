from __future__ import annotations

# Placeholder adapter – in real life you'd do requests/httpx here.
# Keeping it so the folder structure makes sense.

class HttpClient:
    def get(self, url: str) -> str:
        raise NotImplementedError("Dummy service – no real HTTP implemented.")
