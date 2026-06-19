# Persistent Receipt Store

## Purpose

Phase 1 adds a write-once receipt-store boundary for durable receipt handling.

This does not replace enterprise database review. It proves the public runtime has stronger persistence semantics than a mutable demo object.

## Supported Posture

```text
SQLite demo path
filesystem receipt export
immutable proof bundle export
Postgres-ready adapter boundary later
```

## Write-Once Rule

A receipt must not be silently overwritten.

If a correction is required, the runtime must create a new versioned correction event or a new receipt path. It must not mutate the existing receipt in place.

## A+ Pass Condition

Tests must prove:

- receipt can be written once
- receipt cannot be silently overwritten
- receipt can be retrieved by ID
- receipt can be verified after reload
- receipt can be exported into a proof packet
- receipt hash matches the proof packet manifest

Implemented proof file:

```text
tests/test_receipt_store.py
```
