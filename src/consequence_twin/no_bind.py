from __future__ import annotations

from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List


class NoBindError(ValueError):
    """Raised when no-bind proof cannot be produced or validated."""


@dataclass(frozen=True)
class NoBindProof:
    proof_type: str
    movement_attempted: Dict[str, Any]
    reason_admission_failed: List[str]
    missing_or_invalid_standing_condition: str | None
    blocked_consequence_path: str
    route_closure_state: str
    receipt_reference: str | None
    replay_reference: str | None
    downstream_effect_status: str
    timestamp_utc: str

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


def create_no_bind_proof(
    *,
    movement: Dict[str, Any],
    admission_result: Dict[str, Any],
    receipt_reference: str | None = None,
    replay_reference: str | None = None,
    blocked_consequence_path: str = "protected_execution_route",
) -> NoBindProof:
    verdict = str(admission_result.get("verdict", ""))
    if verdict == "ADMIT":
        raise NoBindError("no-bind proof cannot be produced for admitted movement")

    reasons = list(admission_result.get("reasons", [])) or ["admission did not bind"]
    standing_condition = None
    if not movement.get("standing_active", True):
        standing_condition = "standing inactive or expired"
    elif not movement.get("authority_present", True):
        standing_condition = "authority absent"
    elif not movement.get("authority_scope_valid", True):
        standing_condition = "authority outside required scope"

    return NoBindProof(
        proof_type="elyria_no_bind_proof",
        movement_attempted=dict(movement),
        reason_admission_failed=reasons,
        missing_or_invalid_standing_condition=standing_condition,
        blocked_consequence_path=blocked_consequence_path,
        route_closure_state="closed",
        receipt_reference=receipt_reference,
        replay_reference=replay_reference,
        downstream_effect_status="not_activated",
        timestamp_utc=datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
    )


def validate_no_bind_proof(proof: Dict[str, Any]) -> Dict[str, Any]:
    required = [
        "movement_attempted",
        "reason_admission_failed",
        "blocked_consequence_path",
        "route_closure_state",
        "receipt_reference",
        "replay_reference",
        "downstream_effect_status",
    ]
    missing = [field for field in required if field not in proof]
    if missing:
        return {"valid": False, "reason": f"missing fields: {', '.join(missing)}"}
    if proof.get("route_closure_state") != "closed":
        return {"valid": False, "reason": "route not closed"}
    if proof.get("downstream_effect_status") != "not_activated":
        return {"valid": False, "reason": "downstream effect activated"}
    if not proof.get("reason_admission_failed"):
        return {"valid": False, "reason": "missing failure reason"}
    return {"valid": True, "proof_type": proof.get("proof_type")}
