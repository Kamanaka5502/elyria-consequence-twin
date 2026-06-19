from consequence_twin.route_closure import (
    assert_closed_for_refusal,
    can_export_as_admitted,
    create_route_closure_proof,
)


def test_refused_movement_closes_route():
    proof = create_route_closure_proof(
        movement_id="MOVE-001",
        verdict="REFUSE",
        receipt_reference="RCT-001",
    ).to_dict()
    assert proof["route_state"] == "closed"
    assert proof["downstream_state"] == "not_activated"
    assert_closed_for_refusal(proof)


def test_held_movement_closes_route():
    proof = create_route_closure_proof(movement_id="MOVE-002", verdict="HOLD").to_dict()
    assert proof["route_state"] == "closed"
    assert proof["downstream_state"] == "not_activated"


def test_admitted_movement_leaves_route_open():
    proof = create_route_closure_proof(movement_id="MOVE-003", verdict="ADMIT").to_dict()
    assert proof["route_state"] == "open"
    assert proof["downstream_state"] == "eligible_after_admission"


def test_refused_movement_cannot_later_export_as_admitted_without_changed_condition_receipt():
    closure = create_route_closure_proof(
        movement_id="MOVE-004",
        verdict="REFUSE",
        receipt_reference="RCT-OLD",
    ).to_dict()
    assert can_export_as_admitted(original_closure=closure, new_receipt=None) is False


def test_changed_condition_admission_requires_new_receipt():
    closure = create_route_closure_proof(
        movement_id="MOVE-005",
        verdict="REFUSE",
        receipt_reference="RCT-OLD",
    ).to_dict()
    new_receipt = {
        "receipt_id": "RCT-NEW",
        "verdict": "ADMIT",
        "changed_condition_replay": True,
    }
    assert can_export_as_admitted(original_closure=closure, new_receipt=new_receipt) is True
