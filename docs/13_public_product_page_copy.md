# Public Product Page Copy

## Hero

### Elyria Consequence Twin

```text
Know whether action can bind before execution becomes real.
```

Elyria Consequence Twin is a live consequence-admission sandbox for AI, workflow, approval, access, payment, deployment, and customer-operation movement.

It classifies whether a movement may bind, must hold, must be refused, or is attempting to become operationally real without durable proof.

```text
movement -> evidence -> verdict -> signed receipt -> replay -> exposure graph
```

## Primary Call to Action

```text
Request a Consequence Twin Scan
```

Secondary CTA:

```text
View the Demo Proof Surface
```

## The Problem

Modern organizations are moving faster than their proof systems.

AI recommendations, automated approvals, payment releases, customer escalations, access events, policy exceptions, and deployment actions can become operationally real before anyone can prove whether they had authority, standing, evidence, custody, refusal clearance, receipt, or replay basis.

Most systems can tell you what happened.

Elyria asks the higher-risk question:

```text
Was this action allowed to become consequence in the first place?
```

## What Elyria Does

Elyria Consequence Twin models consequence-bearing movement before execution binds.

For each movement, it checks:

```text
authority
standing
evidence
custody
refusal conditions
revalidation triggers
receipt availability
replay availability
```

Then it emits a deterministic verdict:

```text
ADMIT — consequence may bind
HOLD — proof is incomplete
REFUSE — movement is blocked
NO_PROVABLE_ADMISSION — black-path consequence risk
```

## The Black Path

The black path is the executive risk surface.

It shows where action is attempting to become operationally real without durable proof.

Black-path exposure can appear when:

```text
required evidence is missing
custody is not preserved
receipt proof is unavailable
replay proof is unavailable
authority appears to admit movement without evidence
```

## Evidence Attachment Layer

Elyria does not only ask whether evidence exists.

It attaches structured evidence references to the movement itself:

```text
evidence ID
evidence type
source system
custody owner
hash/reference
required vs optional status
accepted / missing / insufficient status
```

The signed receipt includes an evidence summary showing required evidence, accepted evidence, missing evidence, custody gaps, hash references, source systems, and custody owners.

## Signed Receipts and Replay

Every assessed movement emits a signed receipt.

Each receipt preserves:

```text
movement ID
verdict
color
reasons
input hash
original input
evidence summary
engine version
signature algorithm
signature
```

Replay verifies whether the original verdict basis still matches:

```text
input hash matches
verdict basis matches
signature matches
evidence summary matches
```

## Demo Proof Surface

The working demo includes:

```text
client-mode authentication
custom movement intake
structured evidence attachment
signed receipt generation
receipt replay verification
current stored exposure graph
black-path executive warning
proof packet export
```

## Who It Is For

Elyria Consequence Twin is built for teams governing high-consequence movement:

```text
AI governance
compliance
platform engineering
workflow automation
financial operations
healthcare operations
security and access governance
founders building regulated automation
```

## First Offer

### Consequence Twin Scan

A focused diagnostic that maps where AI, workflow, access, approval, payment, deployment, or customer-operation actions may bind consequence without sufficient authority, evidence, custody, standing, receipt, or replay proof.

Deliverables may include:

```text
Consequence Binding Map
Consequence Exposure Graph
Authority Collapse Report
Evidence Gap Register
Refusal Conditions Matrix
Revalidation Trigger Map
Executive Consequence Risk Brief
Implementation Blueprint
```

## Pilot Offer

### Consequence Twin Pilot Corridor

A scoped pilot around one high-consequence movement type.

Example pilot corridors:

```text
AI recommendation -> operator approval
customer escalation -> financial adjustment
policy exception -> workflow override
access request -> privileged action
evidence check -> payment release
model update -> production deployment
```

## Positioning Statement

```text
Elyria Consequence Twin closes the gap between governance documentation and operational consequence control.

It does not merely record what happened.
It proves whether movement had the standing, evidence, custody, receipt, and replay basis required to become real.
```

## Proof Claim

```text
Elyria Consequence Twin classifies consequence-bearing movement before execution binds, attaches evidence references, emits signed receipts, verifies replay basis, and exposes black-path consequence risk before action becomes operationally real.
```

## Footer Boundary

```text
This public demo is a starter runtime and commercial proof surface. It does not expose the full private Elyria runtime, private artifact estate, or proprietary proof corridor.
```
