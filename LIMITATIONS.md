# Limitations

## Public boundary

This repository is a buyer-facing proof surface and runtime demo within Elyria's broader consequence-governance architecture.

It is not the protected Elyria / Veritas kernel, private proof corridor, production enforcement layer, or customer-specific certification environment.

## Not production certification

This repo does not certify that a customer system is production-ready, compliant, legally sufficient, medically safe, financially authorized, or security-certified.

Production use requires:

```text
security review
secret management
deployment review
customer-specific policy mapping
customer-specific evidence mapping
access-control review
logging and retention review
legal/compliance review where applicable
operational acceptance testing
```

## Not substrate claim

This repo does not claim substrate status.

Correct framing:

```text
Elyria is universal at the architecture layer.
This repo is bounded at the proof-surface layer.
```

## Demo signing boundary

Local demo signatures prove that the demo receipt envelope is internally consistent under the configured local signing secret.

They do not prove production custody, enterprise key management, customer approval, or external certification.

## Evidence boundary

The evidence attachment layer accepts structured evidence references and summarizes them into receipts.

It does not store private evidence documents, perform full document validation, replace legal evidence review, or certify external source systems.

## Client-mode boundary

Client mode protects selected demo endpoints with bearer-token authentication.

It is a demo protection layer, not a complete enterprise authentication/authorization system.

## Data boundary

Do not use real customer data, medical data, financial data, legal data, HR data, production secrets, or sensitive operational identifiers in public demos or proof packets.

Use sanitized demo values only.

## Current engineering limits

Known current limits:

```text
SQLite local storage by default
single-process demo runtime
local bearer-token protection
no production key-management integration
no external evidence-store adapter
no enterprise identity provider integration
no customer-specific policy pack
no cloud deployment certification
```

## Correct use

Use this repo to demonstrate:

```text
consequence-admission flow
movement intake
structured evidence references
signed receipt envelope
replay verification
black-path exposure
proof packet export
```

Do not use it to claim:

```text
universal governance proof by itself
production certification
customer-specific compliance certification
protected kernel disclosure
medical, legal, financial, or security certification
```
