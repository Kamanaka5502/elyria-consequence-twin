# External Verifier Guide

## Purpose

The external verifier lets a reviewer inspect a review bundle without starting the Elyria Admission Runtime app.

It checks:

```text
digest manifest equality
sample receipt verification
sample audit-chain verification
sample no-bind proof verification
sample changed-condition replay verification
```

## Command

From repository root:

```bash
python external_verifier/verify_bundle.py review-bundle/latest
```

Expected output:

```text
RESULT: ELYRIA ADMISSION RUNTIME VERIFIER PASS
```

## Boundary

This verifier is a buyer-review verification surface. It does not claim production certification, customer certification, or external audit approval.
