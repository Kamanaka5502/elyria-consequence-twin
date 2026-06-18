# Demo Screenshot and Proof Safety Checklist

## Purpose

Use this checklist before creating screenshots, proof packets, videos, demo clips, or buyer-facing materials.

## Safe Demo Mode

For public screenshots, prefer demo mode unless client-mode protection is being demonstrated.

```bash
unset ELYRIA_MODE
unset ELYRIA_API_TOKEN
unset ELYRIA_RECEIPT_SIGNING_SECRET
uvicorn apps.api.main:app --reload --host 0.0.0.0 --port 8080
```

Safe public screenshots may show:

```text
mode: demo
sample consequence graph
sample receipt cards
sample evidence_summary
sample proof packet structure
black-path warning
```

## Client Mode Demo

For protected-client screenshots:

```bash
export ELYRIA_MODE=client
export ELYRIA_API_TOKEN="local-demo-token-only"
export ELYRIA_RECEIPT_SIGNING_SECRET="local-demo-secret-only"
uvicorn apps.api.main:app --reload --host 0.0.0.0 --port 8080
```

Before screenshot:

```text
confirm token is masked
confirm no raw token appears in output
confirm no shell window exposes ELYRIA_API_TOKEN
confirm no shell window exposes ELYRIA_RECEIPT_SIGNING_SECRET
confirm browser autocomplete has not exposed the token
```

## Never Show Publicly

Do not show:

```text
real client names
real user names
real token values
real signing secrets
real production hashes
real client evidence records
real medical, financial, legal, HR, security, access, or customer data
private paths that expose names or unrelated projects
raw .env files
cloud provider secrets
repository write tokens
```

## Proof Packet Safety

Before exporting a proof packet for public use, confirm the packet contains only demo data.

Safe packet traits:

```text
service metadata only
sample movement IDs
sample evidence IDs
sample receipt IDs
sample signatures from local demo secret only
sample graph paths
no client identifiers
no actual evidence hashes
no production signing secret
```

Unsafe packet traits:

```text
real customer movement IDs
real client source systems
real custody owners tied to a client
real hash references from production documents
real operational receipt IDs from a client environment
real timestamps from sensitive operations
```

## Screenshot Sequence

Recommended public sequence:

```text
1. Open dashboard.
2. Reset Sandbox + Generate Receipts.
3. Preset Missing Evidence.
4. Submit Movement + Emit Receipt.
5. Load Current Stored Graph.
6. Load Receipt Cards.
7. Replay Receipt.
8. Export sanitized proof packet only if using demo data.
```

## Redaction Rules

Before sharing externally:

```text
crop browser bookmarks
hide local path bars
hide terminal command history if secrets were ever typed
hide username if not intentionally branded
clear client token for non-auth screenshots
verify proof packet is demo-only
```

## Public Caption

Safe caption:

```text
Elyria Consequence Twin live demo: classifies consequence-bearing movement before execution binds, attaches evidence references, emits signed receipts, verifies replay basis, and exposes black-path risk before action becomes operationally real.
```

## Buyer Demo Caption

```text
The black path is the review surface. It shows where movement is attempting to become operationally real without sufficient authority, evidence, custody, receipt, or replay proof.
```
