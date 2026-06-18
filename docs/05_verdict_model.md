# Verdict Model

## Required Fields

A consequence movement must be evaluated from explicit fields:

- movement_id
- source_node
- target_node
- consequence_type
- authority_present
- authority_scope_valid
- standing_active
- evidence_present
- evidence_sufficient
- custody_preserved
- refusal_condition_active
- revalidation_required
- receipt_available
- replay_available

## Verdict Logic

### REFUSE

Movement is refused if a hard blocking condition exists.

Examples:

- refusal condition active
- authority absent
- authority outside scope
- standing expired
- prohibited consequence type

### HOLD

Movement is held when it may become admissible but required proof is incomplete.

Examples:

- evidence missing
- evidence insufficient
- custody unclear
- revalidation required before continuation
- receipt missing
- replay not available

### ADMIT

Movement is admitted only when all required dimensions hold.

### NO_PROVABLE_ADMISSION

Movement is classified as no provable admission when consequence can bind without adequate proof of authority, evidence, custody, receipt, or replay.

This is the black-path verdict.
