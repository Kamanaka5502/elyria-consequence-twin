from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, Iterable, List


class TenantIsolationError(PermissionError):
    """Raised when tenant scope is missing or violated."""


@dataclass(frozen=True)
class TenantContext:
    tenant_id: str
    principal_id: str | None = None


def extract_tenant_id(record: Dict[str, Any], *, production_mode: bool = False) -> str | None:
    tenant_id = record.get("tenant_id")
    if tenant_id is None:
        if production_mode:
            raise TenantIsolationError("missing tenant_id in production mode")
        return None
    tenant_id = str(tenant_id).strip()
    if not tenant_id:
        raise TenantIsolationError("blank tenant_id is not valid")
    return tenant_id


def require_tenant(record: Dict[str, Any], *, production_mode: bool = False) -> str:
    tenant_id = extract_tenant_id(record, production_mode=production_mode)
    if tenant_id is None:
        raise TenantIsolationError("tenant_id required")
    return tenant_id


def assert_same_tenant(
    actor_tenant_id: str,
    record: Dict[str, Any],
    *,
    production_mode: bool = False,
) -> None:
    record_tenant_id = require_tenant(record, production_mode=production_mode)
    if record_tenant_id != actor_tenant_id:
        raise TenantIsolationError(
            f"cross-tenant access denied: actor={actor_tenant_id} record={record_tenant_id}"
        )


def filter_records_for_tenant(
    tenant_id: str,
    records: Iterable[Dict[str, Any]],
    *,
    production_mode: bool = False,
) -> List[Dict[str, Any]]:
    scoped: List[Dict[str, Any]] = []
    for record in records:
        record_tenant = extract_tenant_id(record, production_mode=production_mode)
        if record_tenant == tenant_id:
            scoped.append(record)
    return scoped


def attach_tenant(record: Dict[str, Any], tenant_id: str) -> Dict[str, Any]:
    if not str(tenant_id).strip():
        raise TenantIsolationError("tenant_id cannot be blank")
    enriched = dict(record)
    enriched["tenant_id"] = str(tenant_id).strip()
    return enriched
