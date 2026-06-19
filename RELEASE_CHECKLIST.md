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

## Required Verification Before Final A+ Wording

- [ ] `python scripts/verify_all.py` passes locally
- [ ] GitHub Actions pass on `main`
- [ ] `FRESH_CLONE_REVIEW_TEST.md` has terminal evidence pasted
- [ ] `A_PLUS_VERIFICATION_GATE.md` requirements are satisfied
- [ ] Issue #6 final gate checklist is complete
- [ ] release tag is published
- [ ] release description uses bounded buyer-review wording

## Safe Public Release Description

```text
Public release of Elyria Admission Runtime.

This release exposes a bounded buyer-review runtime layer for consequence admission before execution binds, including dashboard intake, API assessment, deterministic verdicting, evidence-gated admission, signed receipts, replay verification, exposure graphing, proof-packet export, external verifier review, digest manifest verification, and production preflight review mode.

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
