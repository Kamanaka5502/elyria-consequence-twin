# Production Readiness Checklist

## Mode and Access

- [ ] `ELYRIA_MODE=client` is set outside sandbox use.
- [ ] `ELYRIA_API_TOKEN` is stored in a secrets manager.
- [ ] Protected endpoints reject unauthenticated requests.
- [ ] Demo mode is used only with public-safe sample data.

## Receipt Integrity

- [ ] `ELYRIA_RECEIPT_SIGNING_SECRET` is set outside source control.
- [ ] Receipts include `signature_algorithm` and `signature`.
- [ ] Replay verifies input hash, verdict basis, and signature.
- [ ] Receipt retention policy is documented.

## Storage

- [ ] SQLite is used only for local sandbox/demo.
- [ ] Managed database is selected for production.
- [ ] Backups are configured.
- [ ] Restore test has been performed.
- [ ] Data retention and deletion policy is documented.

## Deployment

- [ ] HTTPS is active.
- [ ] Environment variables are configured outside source control.
- [ ] Health endpoint is monitored.
- [ ] Error logs are retained.
- [ ] Rollback path is documented.

## Client Boundary

- [ ] No private client material is stored in demo mode.
- [ ] Client artifacts are separated from public-safe demo artifacts.
- [ ] Access review has been completed.
- [ ] Production acceptance evidence is exported and archived.
