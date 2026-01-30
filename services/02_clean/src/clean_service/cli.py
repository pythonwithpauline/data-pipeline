from __future__ import annotations

from pathlib import Path

from .args import parse_cli_args
from .config import CleanConfig
from .io_utils import deep_merge, load_yaml
from .service import run


def main() -> None:
    args = parse_cli_args()

    base_cfg = load_yaml(Path("configs/clean/base.yaml"))
    client_cfg = load_yaml(Path(f"configs/clean/clients/{args.client}.yaml"))
    merged = deep_merge(base_cfg, client_cfg)

    config = CleanConfig.from_dict(merged)
    out_path = run(config)
    print(f"Wrote: {out_path}")
