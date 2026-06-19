from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict


class VerificationError(RuntimeError):
    pass


REQUIRED_FIELDS = [
    "replay_type",
    "original_receipt_id",
    "new_receipt_id",
    "changed_condition_replay",
    "old_receipt_preserved",
    "changed_fields",
    "original_verdict",
    "changed_verdict",
    "reason_for_difference",
]


def verify_replay(replay: Dict[str, Any]) -> Dict[str, Any]:
    missing = [field for field in REQUIRED_FIELDS if field not in replay]
    if missing:
        raise VerificationError(f"replay proof missing fields: {', '.join(missing)}")
    if replay.get("changed_condition_replay") is not True:
        raise VerificationError("changed-condition replay marker missing")
    if replay.get("old_receipt_preserved") is not True:
        raise VerificationError("old receipt preservation marker missing")
    if replay.get("new_receipt_id") == replay.get("original_receipt_id"):
        raise VerificationError("changed-condition replay must reference a new receipt")
    if not replay.get("changed_fields"):
        raise VerificationError("changed-condition replay missing changed fields")
    return {
        "valid": True,
        "original_receipt_id": replay["original_receipt_id"],
        "new_receipt_id": replay["new_receipt_id"],
    }


def verify_replay_file(path: str | Path) -> Dict[str, Any]:
    return verify_replay(json.loads(Path(path).read_text(encoding="utf-8")))


if __name__ == "__main__":
    import sys

    result = verify_replay_file(sys.argv[1])
    print(json.dumps(result, indent=2, sort_keys=True))
