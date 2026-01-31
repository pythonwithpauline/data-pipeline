# A Simple Data Pipeline (services + configs)

This repo contains two small services:

- **01_download**: fetches leads via a dummy HTTP client and writes an Excel file.
- **02_clean**: reads the Excel file, performs tiny cleaning, writes a cleaned Excel file.

## Quickstart (Linux / macOS)

(Ask AI for the respective setup on Windows)


```bash
python -m venv .venv
source .venv/bin/activate

pip install -e services/01_download
pip install -e services/02_clean

# run with a client config (base + client override)
download-service run --client acme
clean-service run --client acme
```

Output:
- `data/raw/leads.xlsx`
- `data/processed/leads_clean.xlsx`

## How config is resolved

Each service loads:

1. `configs/<service>/base.yaml` (defaults)
2. `configs/<service>/clients/<client>.yaml` (client-specific overrides)

The client file overrides keys from base. There are no extra CLI overrides at this moment.
