# Persistent Audit Ledger

## Purpose

Receipt storage is not the same as an audit ledger.

Phase 1 adds an append-only audit-chain model where each event carries the previous event hash.

## Required Event Classes

Minimum event classes include:

```text
movement submitted
evidence evaluated
authority checked
standing checked
verdict issued
receipt signed
replay requested
replay verified
proof packet exported
refusal / no-bind emitted
tamper detected
production preflight failed
```

## Hash-Chain Rule

Each event records:

```text
event_id
event_type
tenant_id
actor_id
timestamp_utc
payload_hash
previous_hash
event_hash
```

## A+ Pass Condition

Tests must prove:

- deleting an event breaks the chain
- editing an event breaks the chain
- reordering events breaks the chain
- missing previous hash fails verification
- tamper detection can emit an explicit event

Implemented proof file:

```text
tests/test_audit_ledger.py
```
