from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Dict, FrozenSet, Iterable, Set


class Role(str, Enum):
    VIEWER = "viewer"
    OPERATOR = "operator"
    REVIEWER = "reviewer"
    ADMIN = "admin"
    AUDITOR = "auditor"
    EXTERNAL_VERIFIER = "external_verifier"


class Permission(str, Enum):
    READ_DASHBOARD = "read_dashboard"
    SUBMIT_MOVEMENT = "submit_movement"
    ISSUE_REVIEW_VERDICT = "issue_review_verdict"
    READ_RECEIPTS = "read_receipts"
    READ_AUDIT_CHAIN = "read_audit_chain"
    VERIFY_PROOF_PACKET = "verify_proof_packet"
    EXPORT_PROOF_PACKET = "export_proof_packet"
    CONFIGURE_RUNTIME = "configure_runtime"


class AuthorizationError(PermissionError):
    """Raised when a role attempts an unauthorized runtime action."""


ROLE_PERMISSIONS: Dict[Role, FrozenSet[Permission]] = {
    Role.VIEWER: frozenset({Permission.READ_DASHBOARD}),
    Role.OPERATOR: frozenset({Permission.READ_DASHBOARD, Permission.SUBMIT_MOVEMENT}),
    Role.REVIEWER: frozenset(
        {
            Permission.READ_DASHBOARD,
            Permission.READ_RECEIPTS,
            Permission.ISSUE_REVIEW_VERDICT,
            Permission.VERIFY_PROOF_PACKET,
        }
    ),
    Role.ADMIN: frozenset(
        {
            Permission.READ_DASHBOARD,
            Permission.READ_RECEIPTS,
            Permission.READ_AUDIT_CHAIN,
            Permission.CONFIGURE_RUNTIME,
        }
    ),
    Role.AUDITOR: frozenset(
        {
            Permission.READ_DASHBOARD,
            Permission.READ_RECEIPTS,
            Permission.READ_AUDIT_CHAIN,
            Permission.VERIFY_PROOF_PACKET,
        }
    ),
    Role.EXTERNAL_VERIFIER: frozenset({Permission.VERIFY_PROOF_PACKET}),
}

# Explicitly forbidden even for admin. Admin configures runtime, but cannot bypass admission.
NON_BYPASSABLE_PERMISSIONS: FrozenSet[Permission] = frozenset(
    {Permission.ISSUE_REVIEW_VERDICT, Permission.SUBMIT_MOVEMENT, Permission.EXPORT_PROOF_PACKET}
)


@dataclass(frozen=True)
class Principal:
    principal_id: str
    role: Role
    tenant_id: str | None = None


def normalize_role(role: Role | str) -> Role:
    try:
        return role if isinstance(role, Role) else Role(str(role))
    except ValueError as exc:
        raise AuthorizationError(f"unknown role: {role}") from exc


def normalize_permission(permission: Permission | str) -> Permission:
    try:
        return permission if isinstance(permission, Permission) else Permission(str(permission))
    except ValueError as exc:
        raise AuthorizationError(f"unknown permission: {permission}") from exc


def permissions_for(role: Role | str) -> Set[Permission]:
    normalized = normalize_role(role)
    return set(ROLE_PERMISSIONS[normalized])


def can(role: Role | str, permission: Permission | str) -> bool:
    normalized_permission = normalize_permission(permission)
    return normalized_permission in permissions_for(role)


def require_permission(principal: Principal, permission: Permission | str) -> None:
    normalized_permission = normalize_permission(permission)
    if not can(principal.role, normalized_permission):
        raise AuthorizationError(
            f"principal {principal.principal_id} with role {principal.role.value} "
            f"cannot perform {normalized_permission.value}"
        )


def require_all(principal: Principal, permissions: Iterable[Permission | str]) -> None:
    for permission in permissions:
        require_permission(principal, permission)


def admin_can_bypass_admission(principal: Principal) -> bool:
    """A hard invariant: admin may configure but cannot bypass admission."""

    return False
