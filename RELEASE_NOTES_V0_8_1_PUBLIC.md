# Elyria Admission Runtime v0.8.1 — Public Buyer-Review Release

## Release Title

```text
Elyria Admission Runtime v0.8.1 — Evidence-Gated Consequence Admission Runtime
```

## Release Classification

```text
Public posture: bounded buyer-review runtime candidate
Verification: CI proof-gates passed with verification report artifact
Production deployment: subject to customer review and external review where required
```

## Release Summary

Elyria Admission Runtime is a full-stack consequence-admission runtime for systems where action should not become operationally real without valid authority, active standing, sufficient evidence, preserved custody, deterministic verdicting, signed receipt, and replayable proof.

This public release exposes a bounded buyer-review runtime layer for consequence admission before execution binds, including dashboard intake, API assessment, deterministic verdicting, structured evidence gates, signed receipts, replay verification, exposure graphing, proof-packet export, policy-pack review, no-bind proof, route closure, changed-condition replay, external verifier review, digest manifest verification, production preflight review mode, and machine-readable verification evidence.

## Verified Release Evidence

CI evidence is recorded in:

```text
verification-evidence/ci-155-verification-report.json
verification-evidence/CI_155_SUMMARY.md
```

The verification report records:

```text
passed: true
final_marker: RESULT: ELYRIA ADMISSION RUNTIME FULL VERIFY PASS
unit tests: passed
generate digest manifest: passed
verify digest manifest: passed
external verifier: passed
production preflight review mode: passed
skipped_tests: false
```

## Reviewer Verification

Primary command:

```bash
python scripts/verify_all.py --report verification-report.json
```

Expected final marker:

```text
RESULT: ELYRIA ADMISSION RUNTIME FULL VERIFY PASS
```

## Core Review Files

```text
README.md
STATUS.md
BUYER_REVIEW_INDEX.md
TRACEABILITY_MATRIX.md
A_PLUS_VERIFICATION_GATE.md
REVIEWER_VERIFICATION.md
RELEASE_CHECKLIST.md
FRESH_CLONE_REVIEW_TEST.md
verification-evidence/CI_155_SUMMARY.md
verification-evidence/ci-155-verification-report.json
```

## Correct Claim Boundary

This release supports bounded buyer-review and portfolio inspection under the repository's proprietary source-available license.

It does not assert production deployment approval.

Production deployment remains subject to customer security approval, deployment review, customer-specific policy mapping, and external review where required.

## Recommended Tag

```text
v0.8.1-public
```

## Recommended Release Description

```text
Public release of Elyria Admission Runtime v0.8.1.

This release exposes a bounded buyer-review runtime layer for consequence admission before execution binds, including dashboard intake, API assessment, deterministic verdicting, evidence-gated admission, signed receipts, replay verification, exposure graphing, proof-packet export, policy-pack review, no-bind proof, route closure, changed-condition replay, external verifier review, digest manifest verification, production preflight review mode, and CI verification evidence.

CI proof-gates passed on main and produced a verification-report artifact confirming unit tests, digest generation, digest verification, external verifier, and production preflight review mode.

This release is public for review and portfolio inspection under the repository's proprietary source-available license. Production deployment remains subject to customer security approval or external audit.
```
