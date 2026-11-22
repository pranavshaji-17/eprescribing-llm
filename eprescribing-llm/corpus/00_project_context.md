SOURCE: Project brief (own work, not an external standard)
URL: n/a

## [PROJ-01] Problem statement
Paper-based and poorly integrated prescribing causes medication errors (illegible handwriting, missed drug interactions and allergies, wrong doses) and leaves controlled substances open to forgery and misuse. Manual processes make it hard to track who prescribed what, verify prescriber identity and prove compliance with rules like the DEA's EPCS. An e-prescribing system lets a verified prescriber create, safety-check, sign and securely send prescriptions to pharmacies using standards such as NCPDP SCRIPT and HL7 FHIR, with a full audit trail, and stays compliant as standards change.

## [PROJ-02] Actors
Primary actor: Prescriber (doctor). Main external actor: Pharmacy system. Supporting actors: Compliance officer, Drug knowledge base (for example First Databank), and Credential provider (identity proofing).

## [PROJ-03] Core functionalities
Four core functionalities: (1) write a prescription, (2) check for problems such as drug interactions and allergies, (3) sign and send, with an extra two-factor check for controlled drugs, (4) keep a record in an audit log.

## [PROJ-04] Use cases and relationships
Nine use cases: Create medication order, Run safety checks, Cancel or change order, Transmit to pharmacy, Sign prescription, Two-factor signing, Verify prescriber ID, Review audit trail, Lock on audit failure. Include relationships: Create order includes Run safety checks; Cancel/change includes Transmit; Transmit includes Sign; Two-factor signing includes Verify prescriber ID. Extend relationships: Two-factor signing extends Sign prescription (only for controlled drugs); Lock on audit failure extends Review audit trail (only when an audit fails).
