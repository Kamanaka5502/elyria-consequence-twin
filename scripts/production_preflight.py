from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Dict

from consequence_twin.preflight import (
    PreflightMode,
    evaluate_preflight,
    require_production_ready,
    review_mode_defaults,
)


def load_config(path: str | None) -> Dict[str, bool]:
    if not path:
        return review_mode_defaults()
    return json.loads(Path(path).read_text(encoding="utf-8"))


def main() -> int:
    parser = argparse.ArgumentParser(description="Run Elyria production preflight")
    parser.add_argument("--mode", choices=["review", "production"], default="review")
    parser.add_argument("--config", default=None)
    args = parser.parse_args()

    config = load_config(args.config)
    if args.mode == "production":
        result = require_production_ready(config)
    else:
        result = evaluate_preflight(config, mode=PreflightMode.REVIEW)

    print(json.dumps(result.to_dict(), indent=2, sort_keys=True))
    if args.mode == "review":
        print("PRODUCTION PREFLIGHT REVIEW MODE PASS")
    else:
        print("PRODUCTION PREFLIGHT PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
