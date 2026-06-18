# Full-Stack Scope

## Attribution

```text
Samantha Revita / Elyria Systems
```

## Full-stack claim

This repository is a full-stack buyer-facing proof surface within Elyria's universal consequence-governance architecture.

It includes:

```text
frontend dashboard
client token panel
client movement intake
evidence attachment UI
FastAPI application layer
deterministic consequence-admission engine
structured evidence summary layer
signed receipt runtime
SQLite storage layer
receipt replay verification
current exposure graph endpoint
proof packet export
test suite
deployment notes
buyer/reviewer documentation
```

## What full-stack means here

Full-stack means this repo is not only a static document, backend script, or isolated verifier.

A reviewer can run the stack locally, open the dashboard, submit a movement, attach evidence references, emit a signed receipt, replay the receipt, render the current graph, and export a proof packet.

## What full-stack does not mean

Full-stack does not mean:

```text
production certification
protected Elyria / Veritas kernel disclosure
enterprise identity integration
production key management
customer-specific compliance certification
regulated legal, medical, financial, or security approval
substrate status
```

## Stack layers

### 1. Interface layer

```text
apps/api/static/index.html
```

Provides:

```text
runtime status pills
client token panel
movement intake form
evidence attachment editor
receipt cards
replay buttons
exposure graph view
proof packet export
```

### 2. API layer

```text
apps/api/main.py
```

Provides:

```text
health check
movement assessment endpoint
receipt list/read endpoints
receipt replay endpoint
demo graph endpoint
current stored graph endpoint
demo proof endpoint
sandbox reset endpoint
```

### 3. Admission engine layer

```text
src/consequence_twin/engine.py
```

Classifies consequence-bearing movement into:

```text
ADMIT
HOLD
REFUSE
NO_PROVABLE_ADMISSION
```

### 4. Evidence layer

```text
src/consequence_twin/evidence.py
```

Summarizes structured evidence references into:

```text
total
required
accepted
missing
insufficient
custody_gaps
hash_references
source_systems
custody_owners
status
reasons
```

### 5. Receipt and replay layer

```text
src/consequence_twin/receipt_runtime.py
```

Provides:

```text
input hashing
signed receipt envelope
HMAC-SHA256 signature
verdict-basis replay
evidence-summary replay
signature verification
```

### 6. Storage layer

```text
src/consequence_twin/storage.py
```

Provides:

```text
SQLite receipt storage
receipt retrieval
receipt replay from store
stored current graph basis
```

### 7. Graph layer

```text
src/consequence_twin/graph.py
```

Builds consequence exposure graphs from movement inputs and receipt-backed current state.

### 8. Test layer

```text
tests/
```

Covers:

```text
engine verdicts
API runtime behavior
client movement intake
evidence layer
signed receipt replay
production/client-mode gates
dashboard static surface
full-stack storage path
```

## Reviewer standard

A reviewer should be able to run:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m pytest tests
uvicorn apps.api.main:app --reload --host 0.0.0.0 --port 8080
```

Expected:

```text
RESULT: PASS
Dashboard loads.
Movement can be submitted.
Evidence can be attached.
Signed receipt is emitted.
Replay verifies.
Current graph updates.
Proof packet exports.
```

## Boundary sentence

```text
Full-stack proof surface, not production certification.
Universal architecture layer, bounded public repo claim.
Samantha Revita / Elyria Systems.
```
