import pytest

from consequence_twin.tenant import (
    TenantIsolationError,
    assert_same_tenant,
    attach_tenant,
    filter_records_for_tenant,
    require_tenant,
)


def test_attach_tenant_adds_tenant_id():
    record = attach_tenant({"movement_id": "MOVE-1"}, "tenant-a")
    assert record["tenant_id"] == "tenant-a"


def test_tenant_a_cannot_read_tenant_b_record():
    record = {"tenant_id": "tenant-b", "receipt_id": "RCT-2"}
    with pytest.raises(TenantIsolationError):
        assert_same_tenant("tenant-a", record, production_mode=True)


def test_filter_records_scopes_to_requested_tenant():
    records = [
        {"tenant_id": "tenant-a", "receipt_id": "A1"},
        {"tenant_id": "tenant-b", "receipt_id": "B1"},
        {"tenant_id": "tenant-a", "receipt_id": "A2"},
    ]
    scoped = filter_records_for_tenant("tenant-a", records, production_mode=True)
    assert [record["receipt_id"] for record in scoped] == ["A1", "A2"]


def test_missing_tenant_id_fails_closed_in_production_mode():
    with pytest.raises(TenantIsolationError):
        require_tenant({"receipt_id": "RCT-1"}, production_mode=True)


def test_blank_tenant_id_is_rejected():
    with pytest.raises(TenantIsolationError):
        attach_tenant({"movement_id": "MOVE-1"}, "   ")
