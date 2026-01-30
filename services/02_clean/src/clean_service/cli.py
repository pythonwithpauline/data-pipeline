from __future__ import annotations

import argparse

from .config import CleanConfig
from .service import run


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="clean-service", description="Dummy cleaning service")
    sub = p.add_subparsers(dest="command", required=True)

    run_p = sub.add_parser("run", help="Run the cleaning step")
    run_p.add_argument("--in", dest="in_path", required=True, help="Input JSONL path")
    run_p.add_argument("--out", dest="out_path", required=True, help="Output JSONL path")
    run_p.add_argument("--no-lowercase-email", action="store_true", help="Disable lowercasing emails")
    run_p.add_argument("--no-strip", action="store_true", help="Disable stripping whitespace")
    return p


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "run":
        cfg = CleanConfig(
            lowercase_email=not args.no_lowercase_email,
            strip_whitespace=not args.no_strip,
        )
        out = run(cfg, in_path=args.in_path, out_path=args.out_path)
        print(f"Wrote: {out}")


if __name__ == "__main__":
    main()
