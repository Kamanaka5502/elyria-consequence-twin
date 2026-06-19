import json
import shutil

import pytest

from external_verifier.verify_audit_chain import VerificationError as AuditVerificationError
from external_verifier.verify_bundle import BundleVerificationError, verify_bundle
from external_verifier.verify_no_bind import VerificationError as NoBindVerificationError
from external_verifier.verify_receipt import VerificationError as ReceiptVerificationError
from external_verifier.verify_replay import VerificationError as ReplayVerificationError
from scripts.generate_digest_manifest import write_manifest


def copy_bundle(tmp_path):
    source = "review-bundle/latest"
    target = tmp_path / "bundle"
    shutil.copytree(source, target)
    write_manifest(target)
    return target


def load_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path, payload):
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def test_external_bundle_verifier_passes_current_bundle(tmp_path):
    bundle = copy_bundle(tmp_path)
    result = verify_bundle(bundle)
    assert result["valid"] is True
    assert result["receipt"]["valid"] is True
    assert result["audit_chain"]["valid"] is True
    assert result["no_bind"]["valid"] is True
    assert result["replay"]["valid"] is True


def test_external_receipt_verifier_rejects_signature_difference(tmp_path):
    bundle = copy_bundle(tmp_path)
    receipt_path = bundle / "sample_receipts" / "receipt_admit.json"
    receipt = load_json(receipt_path)
    receipt["signature"] = "different"
    write_json(receipt_path, receipt)
    write_manifest(bundle)

    with pytest.raises(ReceiptVerificationError):
        verify_bundle(bundle)


def test_external_audit_verifier_rejects_sequence_difference(tmp_path):
    bundle = copy_bundle(tmp_path)
    audit_path = bundle / "sample_audit_chain" / "audit_chain.json"
    audit = load_json(audit_path)
    audit["events"][1]["previous_hash"] = "different"
    write_json(audit_path, audit)
    write_manifest(bundle)

    with pytest.raises(AuditVerificationError):
        verify_bundle(bundle)


def test_external_no_bind_verifier_requires_closure_fields(tmp_path):
    bundle = copy_bundle(tmp_path)
    proof_path = bundle / "sample_no_bind" / "no_bind_refuse.json"
    proof = load_json(proof_path)
    proof.pop("route_closure_state")
    write_json(proof_path, proof)
    write_manifest(bundle)

    with pytest.raises(NoBindVerificationError):
        verify_bundle(bundle)


def test_external_replay_verifier_requires_new_receipt_reference(tmp_path):
    bundle = copy_bundle(tmp_path)
    replay_path = bundle / "sample_replays" / "changed_replay.json"
    replay = load_json(replay_path)
    replay["new_receipt_id"] = replay["original_receipt_id"]
    write_json(replay_path, replay)
    write_manifest(bundle)

    with pytest.raises(ReplayVerificationError):
        verify_bundle(bundle)


def test_external_bundle_verifier_reports_missing_required_file(tmp_path):
    bundle = copy_bundle(tmp_path)
    (bundle / "sample_receipts" / "receipt_admit.json").unlink()
    write_manifest(bundle)

    with pytest.raises(BundleVerificationError):
        verify_bundle(bundle)
