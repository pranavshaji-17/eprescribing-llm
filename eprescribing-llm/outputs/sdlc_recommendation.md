# Recommended SDLC model: Hybrid (V-Model gates + Agile sprints)

Heuristic top choice: **Hybrid (V-Model gates + Agile sprints)** (83.4). LLM agrees with heuristic: **True**.

## Summary

The hybrid model best balances regulatory rigor, safety-critical operations, and evolving standards by integrating the structured validation of V-Model gate reviews with iterative development cycles for flexibility.

## Justification

- Regulatory compliance and audit traceability are enforced through formal verification gates at key lifecycle stages (e.g., prescription creation, signing, transmission), ensuring immutability and alignment with mandated standards like NCPDP SCRIPT and DEA requirements. (evidence: REQ-UC1-02, REQ-UC6-03, REQ-UC7-03, REQ-UC8-04, REQ-UC9-05, REQ-XC-03)
- Safety-critical checks (e.g., drug interactions, allergies) are performed independently and in real time, requiring iterative validation during development to ensure correctness under dynamic conditions. (evidence: REQ-UC2-01, REQ-UC2-05, REQ-XC-02, REQ-XC-06)
- The model supports evolving standards (e.g., NCPDP SCRIPT version upgrades) through iterative delivery cycles that allow for controlled integration and testing of new mandates without disrupting core operations. (evidence: REQ-UC3-05, REQ-UC4-03, REQ-XC-01)
- Audit trail requirements are met through both formal gate reviews and continuous logging, ensuring traceability across all actions including identity verification, signing, and transmission events. (evidence: REQ-UC6-03, REQ-UC8-01, REQ-UC8-02, REQ-UC8-03, REQ-UC9-03)

## Why not the others

- **V-Model:** While the V-Model provides strong structure for compliance and traceability, it lacks flexibility to adapt to evolving standards or real-time safety alerts during prescription creation, which are dynamically assessed and require iterative feedback loops.
- **Spiral:** The Spiral model emphasizes risk analysis but does not provide sufficient built-in mechanisms for regulatory audit trail integrity or traceability of controlled substance actions, which are mandatory and time-bound (e.g., 7-year retention).
- **Incremental/Iterative:** This model lacks formal gate reviews that ensure compliance with strict regulatory requirements such as two-factor authentication for controlled substances or audit failure locking mechanisms, risking non-compliance in high-risk scenarios.
- **Waterfall:** The linear nature of Waterfall prevents early detection and correction of safety-critical issues (e.g., real-time interaction alerts) and fails to support iterative integration of new standards or regulatory updates during development.
- **Agile (Scrum):** While agile supports iteration, it lacks the formal verification gates required for compliance with immutable audit trails, controlled substance locking, and mandatory two-factor authentication enforcement at specific lifecycle points.

## Tailored process

- **Requirements Specification:** Finalize all functional and regulatory requirements in a traceable matrix; map each requirement to its source (e.g., REQ-UC6-01, REQ-XC-04) and ensure alignment with controlled substance policies and audit standards.
- **Design & Architecture:** Define system architecture with secure identity verification, real-time safety checks, and immutable audit logging; implement modular components for drug interaction logic and NCPDP SCRIPT message generation.
- **Implementation (Sprint Cycles):** Develop core features in short sprints (e.g., prescription creation, safety check alerts), with each sprint validated against regulatory requirements such as two-factor authentication and real-time interaction detection.
- **Formal Verification Gates:** At key milestones (e.g., after safety checks, signing, transmission), conduct V-Model-style gate reviews to validate compliance with REQ-UC1-04, REQ-UC5-03, REQ-XC-03, and audit trail integrity requirements.
- **Testing & Compliance Validation:** Perform end-to-end testing of prescription lifecycle including cancellation, change requests, and audit failure scenarios; validate that all events are logged with timestamps, user IDs, and action types as per REQ-UC8-04 and REQ-UC9-05.
- **Deployment & Monitoring:** Deploy in phases with continuous monitoring of audit trails and real-time alerts; support third-party audits every two years or after significant changes (REQ-UC8-05).

## Risks and mitigations

- **Failure to meet regulatory retention periods for audit logs:** Implement automated logging and storage with encrypted, immutable records retained for at least seven years as required by REQ-UC8-03.
- **Inadequate real-time safety check enforcement during prescription creation:** Embed real-time drug interaction checks using an external knowledge base (REQ-XC-06) and validate in each sprint with test cases that simulate allergy and interaction scenarios.
- **Non-compliance due to failure to enforce two-factor authentication for controlled substances:** Enforce REQ-UC6-02 and REQ-UC7-02 at the identity verification gate; require separate device-based authentication and log both factors per REQ-UC6-03.
- **Loss of audit trail integrity during system updates or upgrades:** Ensure all changes to the system are reviewed through formal gates, with full audit trail logging before and after each update (REQ-UC8-05).

## Assumptions

- The external drug knowledge base is available and accessible in real time during prescription creation.
- The NCPDP SCRIPT standard will not undergo abrupt or disruptive changes that require immediate rework of transmission logic.
- Prescriber identity verification via credential provider is interoperable with the e-prescribing platform using standardized protocols (e.g., OAuth, SAML).
