# Fresh Clone Review Test

## Purpose

This file records the clean-machine review path for Elyria Admission Runtime.

## Manual Fresh Clone Commands

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

## Expanded Verification Path

The full verifier runs:

```text
python -m pytest
python scripts/generate_digest_manifest.py review-bundle/latest
python scripts/verify_digest_manifest.py review-bundle/latest
python external_verifier/verify_bundle.py review-bundle/latest
python scripts/production_preflight.py --mode review
```

## Expected Output

```text
pytest PASS
DIGEST MANIFEST PASS
RESULT: ELYRIA ADMISSION RUNTIME VERIFIER PASS
PRODUCTION PREFLIGHT REVIEW MODE PASS
RESULT: ELYRIA ADMISSION RUNTIME FULL VERIFY PASS
```

## Hosted Fresh-Checkout Evidence

GitHub Actions `ci #155` provides hosted fresh-checkout evidence.

Recorded run evidence:

```text
workflow: ci
run: #155
commit: 0ba1635
branch: main
status: Success
job: proof-gates — green
artifact: verification-report
```

The workflow performs a clean GitHub-hosted checkout, installs the package, and runs:

```bash
python scripts/verify_all.py --report verification-report.json
```

The uploaded verification report is recorded in:

```text
verification-evidence/ci-155-verification-report.json
verification-evidence/CI_155_SUMMARY.md
```

Report result:

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

## Evidence Status

```text
hosted fresh-checkout verification: recorded
manual local fresh-clone verification: optional additional evidence
```
