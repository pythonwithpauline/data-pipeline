from __future__ import annotations

import argparse


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="clean-service", description="Clean leads Excel and write output Excel.")
    sub = p.add_subparsers(dest="command", required=True)

    run_p = sub.add_parser("run", help="Run the clean service")
    run_p.add_argument("--client", required=True, choices=["acme", "globex"], help="Client config to use")
    return p


def parse_cli_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = build_parser()
    return parser.parse_args(argv)
