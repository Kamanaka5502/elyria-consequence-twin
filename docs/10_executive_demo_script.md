# Executive Demo Script

## Purpose

This script demonstrates Elyria Consequence Twin as a working proof surface, not a static governance document.

The demo claim:

```text
Elyria Consequence Twin classifies consequence-bearing movement before execution binds, attaches evidence references, emits signed receipts, verifies replay basis, and exposes black-path consequence risk before action becomes operationally real.
```

## Setup

Run in client mode for the protected demo:

```bash
export ELYRIA_MODE=client
export ELYRIA_API_TOKEN="replace-with-local-demo-token"
export ELYRIA_RECEIPT_SIGNING_SECRET="replace-with-local-signing-secret"
uvicorn apps.api.main:app --reload --host 0.0.0.0 --port 8080
```

Open:

```text
http://localhost:8080
```

## Opening Talk Track

```text
This is Elyria Consequence Twin.

It is not a dashboard that only records what happened.
It is a consequence-admission surface that asks whether a movement has enough authority, standing, evidence, custody, refusal clearance, receipt, and replay basis before execution becomes operationally real.

The point is simple: action should not bind consequence unless the system can prove why it was allowed to bind.
```

## Step 1 — Prove Client Mode

Action:

```text
Enter the local demo token.
Click Save Token Locally.
Click Test Protected Access.
```

Expected result:

```text
Protected access OK.
```

Talk track:

```text
The demo is running in client mode. Protected operations require a bearer token. Receipt access, replay, proof export, sandbox reset, and movement assessment are not open in client mode.
```

## Step 2 — Reset Sandbox

Action:

```text
Click Reset Sandbox + Generate Receipts.
Click Load Receipt Cards.
```

Expected result:

```text
Three baseline movements appear:
MOVE-001 / ADMIT / green
MOVE-002 / NO_PROVABLE_ADMISSION / black
MOVE-003 / REFUSE / red
```

Talk track:

```text
The sandbox creates three consequence paths: one admitted, one refused, and one black path. The black path is the important executive risk surface. It shows a movement attempting to become real without durable proof.
```

## Step 3 — Submit Accepted Evidence Movement

Action:

```text
Click Preset Accepted Evidence.
Click Submit Movement + Emit Receipt.
Click Load Current Stored Graph.
Click Load Receipt Cards.
```

Expected result:

```text
A client movement is admitted.
A signed receipt is created.
The current graph updates from stored receipts.
Receipt card shows evidence_summary.
```

Talk track:

```text
This is a client-entered movement, not hardcoded demo output. The movement carries structured evidence references, and the receipt includes an evidence summary inside the signed envelope.
```

## Step 4 — Submit Missing Evidence Movement

Action:

```text
Click Preset Missing Evidence.
Click Preset Black Path if demonstrating full black-path risk.
Click Submit Movement + Emit Receipt.
Click Load Current Stored Graph.
Click Load Receipt Cards.
```

Expected result:

```text
Black Paths increases.
Receipt card shows evidence status: attention_required.
Missing evidence and custody gaps are visible.
```

Talk track:

```text
This is the consequence twin doing the job: it exposes where a movement lacks durable evidence, custody, receipt, or replay proof before action becomes operationally real.
```

## Step 5 — Replay Receipt

Action:

```text
Click Replay Receipt on the newest receipt.
```

Expected result:

```text
input_hash_matches: true
verdict_matches: true
signature_matches: true
evidence_summary_matches: true
```

Talk track:

```text
Replay proves the verdict basis has not drifted. The input hash, verdict, signature, and evidence summary all verify against the stored receipt.
```

## Step 6 — Export Proof Packet

Action:

```text
Click Export Proof Packet.
```

Expected result:

```text
A JSON proof packet downloads with service metadata, current graph, receipts, signatures, evidence summaries, and proof claim.
```

Talk track:

```text
The output is a replayable proof packet. It can be reviewed after the fact, attached to an implementation review, or used as an executive evidence surface for consequence-bearing operations.
```

## Closing Talk Track

```text
The core value is not that Elyria records activity.

The value is that it classifies whether consequence-bearing movement can bind before execution becomes real, shows exactly where proof collapses, emits a signed receipt, and preserves replay evidence.

That is the gap between governance documentation and operational consequence control.
```

## Do Not Show

Do not show:

```text
real tokens
real signing secrets
private client evidence
client production identifiers
private hashes
non-demo proof packets
local filesystem paths containing sensitive names
```
