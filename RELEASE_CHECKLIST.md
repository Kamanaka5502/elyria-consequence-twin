# Release Checklist

## Purpose

This checklist defines the release posture for Elyria Admission Runtime.

Use it before publishing or updating a public release.

## Required Release Naming

Release title should use:

```text
Elyria Admission Runtime
```

Recommended title:

```text
Elyria Admission Runtime v0.8.1 — Evidence-Gated Consequence Admission Runtime
```

Recommended tag:

```text
v0.8.1-public
```

## Required Verification Before Final A+ Wording

- [x] CI verification report passes
- [x] GitHub Actions pass on `main`
- [x] digest verification passes in CI report
- [x] external verifier passes in CI report
- [x] production preflight review mode passes in CI report
- [ ] `FRESH_CLONE_REVIEW_TEST.md` has terminal evidence pasted
- [ ] release tag is published
- [ ] release description uses bounded buyer-review wording
- [ ] Issue #6 final gate checklist is complete

## Release Material Files

```text
RELEASE_NOTES_V0_8_1_PUBLIC.md
RELEASE_PUBLICATION_STEPS.md
verification-evidence/CI_155_SUMMARY.md
verification-evidence/ci-155-verification-report.json
```

## Safe Public Release Description

```text
Public release of Elyria Admission Runtime v0.8.1.

This release exposes a bounded buyer-review runtime layer for consequence admission before execution binds, including dashboard intake, API assessment, deterministic verdicting, evidence-gated admission, signed receipts, replay verification, exposure graphing, proof-packet export, policy-pack review, no-bind proof, route closure, changed-condition replay, external verifier review, digest manifest verification, production preflight review mode, and CI verification evidence.

CI proof-gates passed on main and produced a verification-report artifact confirming unit tests, digest generation, digest verification, external verifier, and production preflight review mode.

This release is public for review and portfolio inspection under the repository's proprietary source-available license. Production deployment remains subject to customer security approval or external audit.
```

## Do Not Use As Release Claims

```text
production certified
customer certified
regulatory approved
third-party audited
full production deployment approved
```

## Final Release Boundary

```text
A+ bounded buyer-review candidate after verification evidence is recorded.
Production deployment subject to customer approval and external review where required.
```
