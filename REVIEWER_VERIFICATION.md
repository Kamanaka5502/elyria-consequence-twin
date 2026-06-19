# Reviewer Verification

## Purpose

This file gives reviewers one clean path to verify the Elyria Admission Runtime buyer-review surface.

It is designed for fresh clone review, GitHub Actions review, and local proof-gate review.

## One-Command Verification

From repository root:

```bash
python scripts/verify_all.py
```

The verifier runs:

```text
unit tests
digest manifest generation
digest manifest verification
external verifier
production preflight review mode
```

Expected final marker:

```text
RESULT: ELYRIA ADMISSION RUNTIME FULL VERIFY PASS
```

## Fresh Clone Review

```bash
git clone https://github.com/Kamanaka5502/elyria-admission-runtime.git
cd elyria-admission-runtime
python -m venv .venv
. .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m pip install -e .
python scripts/verify_all.py
```

## Manual Expanded Path

```bash
python -m pytest
python scripts/generate_digest_manifest.py review-bundle/latest
python scripts/verify_digest_manifest.py review-bundle/latest
python external_verifier/verify_bundle.py review-bundle/latest
python scripts/production_preflight.py --mode review
```

## Expected Evidence Markers

```text
pytest PASS
DIGEST MANIFEST PASS
RESULT: ELYRIA ADMISSION RUNTIME VERIFIER PASS
PRODUCTION PREFLIGHT REVIEW MODE PASS
RESULT: ELYRIA ADMISSION RUNTIME FULL VERIFY PASS
```

## Boundary

Passing reviewer verification supports the A+ bounded buyer-review candidate claim after evidence is recorded.

It does not assert production deployment approval.
