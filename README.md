# data-pipeline (dummy example)

This is a tiny dummy pipeline that demonstrates a service-based repo layout.

Services included:
- `01_download` – writes a small `leads.jsonl` file to an output path
- `02_clean` – reads `leads.jsonl`, applies simple cleaning, writes `leads_clean.jsonl`

Quickstart (from repo root):

```bash
python -m venv .venv
source .venv/bin/activate

pip install -e services/01_download
pip install -e services/02_clean

download-service run --out data/raw/leads.jsonl
clean-service run --in data/raw/leads.jsonl --out data/processed/leads_clean.jsonl
```

Notes:
- These services are deliberately minimal.
- No tests, no dev/prod layering yet.
