import pytest

from consequence_twin.authz import (
    AuthorizationError,
    Permission,
    Principal,
    Role,
    admin_can_bypass_admission,
    can,
    require_permission,
)


def test_viewer_can_read_only():
    assert can(Role.VIEWER, Permission.READ_DASHBOARD)
    assert not can(Role.VIEWER, Permission.SUBMIT_MOVEMENT)
    assert not can(Role.VIEWER, Permission.EXPORT_PROOF_PACKET)


def test_operator_can_submit_but_not_export_or_review():
    assert can(Role.OPERATOR, Permission.SUBMIT_MOVEMENT)
    assert not can(Role.OPERATOR, Permission.ISSUE_REVIEW_VERDICT)
    assert not can(Role.OPERATOR, Permission.EXPORT_PROOF_PACKET)


def test_reviewer_can_issue_review_verdict_without_admin_config():
    assert can(Role.REVIEWER, Permission.ISSUE_REVIEW_VERDICT)
    assert can(Role.REVIEWER, Permission.VERIFY_PROOF_PACKET)
    assert not can(Role.REVIEWER, Permission.CONFIGURE_RUNTIME)


def test_auditor_can_inspect_receipts_and_chain():
    assert can(Role.AUDITOR, Permission.READ_RECEIPTS)
    assert can(Role.AUDITOR, Permission.READ_AUDIT_CHAIN)
    assert not can(Role.AUDITOR, Permission.SUBMIT_MOVEMENT)


def test_external_verifier_can_verify_only():
    assert can(Role.EXTERNAL_VERIFIER, Permission.VERIFY_PROOF_PACKET)
    assert not can(Role.EXTERNAL_VERIFIER, Permission.READ_RECEIPTS)
    assert not can(Role.EXTERNAL_VERIFIER, Permission.EXPORT_PROOF_PACKET)


def test_admin_can_configure_but_cannot_silently_bypass_admission():
    admin = Principal(principal_id="admin-1", role=Role.ADMIN, tenant_id="tenant-a")
    assert can(Role.ADMIN, Permission.CONFIGURE_RUNTIME)
    assert not can(Role.ADMIN, Permission.SUBMIT_MOVEMENT)
    assert not can(Role.ADMIN, Permission.ISSUE_REVIEW_VERDICT)
    assert admin_can_bypass_admission(admin) is False


def test_unauthorized_permission_raises():
    viewer = Principal(principal_id="viewer-1", role=Role.VIEWER, tenant_id="tenant-a")
    with pytest.raises(AuthorizationError):
        require_permission(viewer, Permission.SUBMIT_MOVEMENT)
