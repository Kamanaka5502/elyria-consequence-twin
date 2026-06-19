from __future__ import annotations

import hashlib
import json
import uuid
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from typing import Any, Dict, Iterable, List


class AuditLedgerError(RuntimeError):
    """Raised when an audit chain cannot be verified."""


@dataclass(frozen=True)
class AuditEvent:
    event_id: str
    event_type: str
    tenant_id: str
    actor_id: str
    timestamp_utc: str
    payload_hash: str
    previous_hash: str
    event_hash: str

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


def canonical_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def sha256_json(value: Any) -> str:
    return hashlib.sha256(canonical_json(value).encode("utf-8")).hexdigest()


def event_material(event: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "event_id": event["event_id"],
        "event_type": event["event_type"],
        "tenant_id": event["tenant_id"],
        "actor_id": event["actor_id"],
        "timestamp_utc": event["timestamp_utc"],
        "payload_hash": event["payload_hash"],
        "previous_hash": event["previous_hash"],
    }


def compute_event_hash(event: Dict[str, Any]) -> str:
    return sha256_json(event_material(event))


def append_event(
    chain: Iterable[Dict[str, Any]],
    *,
    event_type: str,
    tenant_id: str,
    actor_id: str,
    payload: Dict[str, Any],
) -> AuditEvent:
    events = list(chain)
    previous_hash = events[-1]["event_hash"] if events else "GENESIS"
    unsigned = {
        "event_id": f"AUD-{uuid.uuid4().hex[:16].upper()}",
        "event_type": event_type,
        "tenant_id": tenant_id,
        "actor_id": actor_id,
        "timestamp_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "payload_hash": sha256_json(payload),
        "previous_hash": previous_hash,
    }
    return AuditEvent(**unsigned, event_hash=sha256_json(unsigned))


def verify_chain(chain: Iterable[Dict[str, Any]]) -> Dict[str, Any]:
    events = list(chain)
    previous_hash = "GENESIS"
    for index, event in enumerate(events):
        if event.get("previous_hash") != previous_hash:
            return {
                "valid": False,
                "index": index,
                "reason": "previous_hash mismatch",
                "event_id": event.get("event_id"),
            }
        expected = compute_event_hash(event)
        if event.get("event_hash") != expected:
            return {
                "valid": False,
                "index": index,
                "reason": "event_hash mismatch",
                "event_id": event.get("event_id"),
            }
        previous_hash = event["event_hash"]
    return {"valid": True, "event_count": len(events), "tip_hash": previous_hash}


def require_valid_chain(chain: Iterable[Dict[str, Any]]) -> None:
    result = verify_chain(chain)
    if not result["valid"]:
        raise AuditLedgerError(str(result))


def tamper_detected_event(
    chain: Iterable[Dict[str, Any]],
    *,
    tenant_id: str,
    actor_id: str,
    verification_result: Dict[str, Any],
) -> AuditEvent:
    return append_event(
        chain,
        event_type="tamper detected",
        tenant_id=tenant_id,
        actor_id=actor_id,
        payload=verification_result,
    )
