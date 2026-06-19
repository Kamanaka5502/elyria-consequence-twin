# Threat Model

## Purpose

This threat model identifies review-relevant risks for Elyria Admission Runtime.

## Review Risks

| Risk | Control Surface |
|---|---|
| unauthorized movement submission | RBAC tests |
| cross-tenant data access | tenant isolation tests |
| receipt material mismatch | receipt verifier |
| audit sequence mismatch | audit-chain verifier |
| replay mismatch | changed-condition replay tests |
| proof packet leakage | deployment checklist |
| evidence privacy exposure | sanitized review bundle |
| debug mode enabled in production | production preflight |
| incomplete production controls | production preflight |
| customer policy mismatch | policy-pack review |

## Boundary

This threat model is a buyer-review artifact. It is not a substitute for customer-specific threat modeling or external security review.
