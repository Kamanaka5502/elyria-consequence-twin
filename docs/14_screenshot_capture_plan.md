# Screenshot Capture Plan

## Purpose

Create a clean buyer-facing screenshot set for Elyria Consequence Twin without exposing secrets, client data, or private local context.

## Capture Mode

Use demo mode for public screenshots unless intentionally showing protected-client behavior.

```bash
unset ELYRIA_MODE
unset ELYRIA_API_TOKEN
unset ELYRIA_RECEIPT_SIGNING_SECRET
uvicorn apps.api.main:app --reload --host 0.0.0.0 --port 8080
```

Use client mode only for a protected-access screenshot.

```bash
export ELYRIA_MODE=client
export ELYRIA_API_TOKEN="local-demo-token-only"
export ELYRIA_RECEIPT_SIGNING_SECRET="local-demo-secret-only"
uvicorn apps.api.main:app --reload --host 0.0.0.0 --port 8080
```

## Pre-Capture Checklist

Before taking any screenshot:

```text
clear browser bookmarks from frame
hide terminal windows
hide local filesystem paths
clear or mask token field
use only sample movement IDs
use only sample evidence IDs
use only demo source systems
use only demo custody owners
verify no raw signing secret appears anywhere
verify no client/private proof packet is open
```

## Screenshot Set

### 1. Hero Dashboard

Capture:

```text
title
runtime status pills
high-level dashboard framing
```

Purpose:

```text
Shows Elyria as a polished live product surface.
```

### 2. Client Token Panel

Capture:

```text
Mode: client
Storage: sqlite
Auth: token stored locally
Client Token Panel with masked token
```

Purpose:

```text
Shows protected demo boundary without exposing the token.
```

### 3. Client Movement Intake

Capture:

```text
movement ID
source node
target node
authority / standing / evidence / custody fields
```

Purpose:

```text
Shows the system accepts client-entered movement, not only preset data.
```

### 4. Evidence Attachment Layer

Capture:

```text
Evidence Items JSON
accepted evidence example
missing evidence example if needed
```

Purpose:

```text
Shows evidence is structured, referenced, and summarized.
```

### 5. Black-Path Executive Warning

Capture after using Preset Black Path:

```text
Black Paths: 2
Executive Warning
NO_PROVABLE_ADMISSION path in graph
```

Purpose:

```text
Shows the value proposition: expose unprovable consequence movement before it binds.
```

### 6. Receipt Card With Evidence Summary

Capture:

```text
NO_PROVABLE_ADMISSION receipt
Signature: HMAC-SHA256
Evidence: attention_required
required / accepted / missing / custody gaps
reasons list
```

Purpose:

```text
Shows receipt, signature, and evidence status in one view.
```

### 7. Replay Verification Output

Capture after clicking Replay Receipt:

```text
input_hash_matches: true
verdict_matches: true
signature_matches: true
evidence_summary_matches: true
```

Purpose:

```text
Shows the proof can be replayed.
```

### 8. Proof Packet JSON

Capture a sanitized section only:

```text
service metadata
graph summary
one receipt with evidence_summary
proof_claim
```

Purpose:

```text
Shows exportable proof packet structure.
```

## Recommended Capture Order

```text
1. Reset Sandbox + Generate Receipts
2. Preset Accepted Evidence
3. Submit Movement + Emit Receipt
4. Preset Black Path
5. Submit Movement + Emit Receipt
6. Load Current Stored Graph
7. Load Receipt Cards
8. Replay newest black-path receipt
9. Export Proof Packet if data is demo-only
```

## Public Caption Set

### Caption 1

```text
Elyria Consequence Twin live proof surface: movement intake, evidence references, signed receipt, replay verification, and black-path exposure before consequence binds.
```

### Caption 2

```text
The black path is the executive risk surface: action attempting to become operationally real without sufficient evidence, custody, receipt, or replay proof.
```

### Caption 3

```text
This is the gap between governance documentation and operational consequence control.
```

## File Naming

```text
01_elyria_dashboard_hero.png
02_client_mode_token_gate.png
03_client_movement_intake.png
04_evidence_attachment_layer.png
05_black_path_warning.png
06_signed_receipt_evidence_summary.png
07_replay_verification.png
08_sanitized_proof_packet.png
```
