from __future__ import annotations

import argparse


def build_parser() -> argparse.ArgumentParser:
    # 1. Create the root parser
    # This is what prints download-service --help.
    p = argparse.ArgumentParser(
        prog="download-service", description="Download leads and write Excel."
    )

    # 2. Add subparsers
    # This creates a registry for commands like run, init, status, etc.
    # dest is the attribute name where argparse stores which command was chosen.
    sub = p.add_subparsers(dest="command", required=True)

    # 3. Create a subcommand parser (run)
    # This makes download-service run --help work.
    # Everything you add here belongs only to run
    run_p = sub.add_parser("run", help="Run the download service")
    run_p.add_argument(
        "--client",
        required=True,
        choices=["acme", "globex"],
        help="Client config to use",
    )

    return p


def parse_cli_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = build_parser()
    return parser.parse_args(argv)
