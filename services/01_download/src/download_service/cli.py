from __future__ import annotations

import argparse

from .config import DownloadConfig
from .service import run


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="download-service", description="Dummy download service")
    sub = p.add_subparsers(dest="command", required=True)

    run_p = sub.add_parser("run", help="Run the download step")
    run_p.add_argument("--out", required=True, help="Output path, e.g. data/raw/leads.jsonl")
    run_p.add_argument("--n-leads", type=int, default=5, help="How many dummy leads to generate")
    return p


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "run":
        cfg = DownloadConfig(n_leads=args.n_leads)
        out = run(cfg, out_path=args.out)
        print(f"Wrote: {out}")


if __name__ == "__main__":
    main()
