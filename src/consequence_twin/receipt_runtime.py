from __future__ import annotations

import hashlib
import json
import uuid
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List

from .engine import assess_movement

ENGINE_VERSION = "0.1.0"


def canonical_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def sha256_json(value: Any) -> str:
    return hashlib.sha256(canonical_json(value).encode("utf-8")).hexdigest()


@dataclass(frozen=True)
class ReceiptRecord:
    receipt_id: str
    movement_id: str
    verdict: str
    color: str
    reasons: List[str]
    timestamp_utc: str
    input_hash: str
    engine_version: str
    original_input: Dict[str, Any]

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


def create_receipt(payload: Dict[str, Any]) -> ReceiptRecord:
    result = assess_movement(payload)
    return ReceiptRecord(
        receipt_id=f"RCT-{uuid.uuid4().hex[:16].upper()}",
        movement_id=result.movement_id,
        verdict=result.verdict.value,
        color=result.color,
        reasons=result.reasons,
        timestamp_utc=datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        input_hash=sha256_json(payload),
        engine_version=ENGINE_VERSION,
        original_input=dict(payload),
    )


def verify_receipt(record: Dict[str, Any]) -> Dict[str, Any]:
    payload = record["original_input"]
    result = assess_movement(payload).to_dict()
    matches = (
        result["movement_id"] == record["movement_id"]
        and result["verdict"] == record["verdict"]
        and result["color"] == record["color"]
        and result["reasons"] == record["reasons"]
    )
    return {
        "receipt_id": record["receipt_id"],
        "input_hash_matches": sha256_json(payload) == record["input_hash"],
        "verdict_matches": matches,
        "actual": result,
    }
