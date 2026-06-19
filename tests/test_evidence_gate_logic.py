from copy import deepcopy

from consequence_twin.engine import assess_movement
from consequence_twin.receipt_runtime import create_receipt, verify_receipt


BASE_PAYLOAD = {
    "movement_id": "EVIDENCE-GATE-001",
    "source_node": "client.workflow",
    "target_node": "governed.action",
    "authority_present": True,
    "authority_scope_valid": True,
    "standing_active": True,
    "evidence_present": True,
    "evidence_sufficient": True,
    "custody_preserved": True,
    "refusal_condition_active": False,
    "revalidation_required": False,
    "receipt_available": True,
    "replay_available": True,
    "notes": "Evidence gate test movement.",
    "evidence_items": [
        {
            "evidence_id": "EV-GATE-001",
            "evidence_type": "policy_record",
            "source_system": "client.registry",
            "custody_owner": "operations.owner",
            "hash_reference": "sha256:gate-reference",
            "required": True,
            "status": "accepted",
            "notes": "Required accepted evidence.",
        }
    ],
}


def payload_with_evidence_item(**updates):
    payload = deepcopy(BASE_PAYLOAD)
    payload["evidence_items"][0].update(updates)
    return payload


def test_accepted_structured_evidence_allows_admit():
    result = assess_movement(BASE_PAYLOAD).to_dict()
    assert result["verdict"] == "ADMIT"
    assert result["color"] == "green"


def test_required_missing_structured_evidence_becomes_black_path_even_if_boolean_flags_claim_ready():
    payload = payload_with_evidence_item(
        evidence_id="EV-GATE-MISSING",
        status="missing",
        custody_owner="operations.owner",
        hash_reference="sha256:gate-reference",
    )
    result = assess_movement(payload).to_dict()
    assert result["verdict"] == "NO_PROVABLE_ADMISSION"
    assert result["color"] == "black"
    assert "required structured evidence missing while authority could bind movement" in result["reasons"]
    assert "required evidence missing: EV-GATE-MISSING" in result["reasons"]


def test_required_insufficient_structured_evidence_holds_movement():
    payload = payload_with_evidence_item(
        evidence_id="EV-GATE-INSUFFICIENT",
        status="insufficient",
    )
    result = assess_movement(payload).to_dict()
    assert result["verdict"] == "HOLD"
    assert result["color"] == "yellow"
    assert "required evidence insufficient: EV-GATE-INSUFFICIENT" in result["reasons"]


def test_required_structured_evidence_without_custody_owner_holds_movement():
    payload = payload_with_evidence_item(
        evidence_id="EV-GATE-CUSTODY",
        custody_owner="",
    )
    result = assess_movement(payload).to_dict()
    assert result["verdict"] == "HOLD"
    assert result["color"] == "yellow"
    assert "required evidence lacks custody owner: EV-GATE-CUSTODY" in result["reasons"]


def test_required_structured_evidence_without_hash_reference_holds_movement():
    payload = payload_with_evidence_item(
        evidence_id="EV-GATE-HASH",
        hash_reference="",
    )
    result = assess_movement(payload).to_dict()
    assert result["verdict"] == "HOLD"
    assert result["color"] == "yellow"
    assert "required evidence lacks hash/reference: EV-GATE-HASH" in result["reasons"]


def test_receipt_replay_verifies_evidence_gate_verdict_basis():
    payload = payload_with_evidence_item(
        evidence_id="EV-GATE-MISSING-REPLAY",
        status="missing",
        custody_owner="operations.owner",
        hash_reference="sha256:gate-reference",
    )
    receipt = create_receipt(payload).to_dict()
    assert receipt["verdict"] == "NO_PROVABLE_ADMISSION"
    assert receipt["evidence_summary"]["status"] == "attention_required"
    check = verify_receipt(receipt)
    assert check["input_hash_matches"] is True
    assert check["verdict_matches"] is True
    assert check["signature_matches"] is True
    assert check["evidence_summary_matches"] is True
