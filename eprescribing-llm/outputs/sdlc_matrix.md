# SDLC decision matrix

Heuristic decision support, not measured probabilities. Weights = the LLM's demand ratings derived from the generated requirements; fit scores are a textbook-informed table in `domain.py`.

## 1. Project demand profile (from requirements)

| Criterion | Rating | Evidence |
|---|---|---|
| upfront_definition | 5 | REQ-UC1-01, REQ-UC1-02, REQ-UC1-03, REQ-UC1-04, REQ-UC2-01, REQ-UC2-02, REQ-UC2-05, REQ-UC2-06, REQ-UC3-01, REQ-UC3-02, REQ-UC3-03, REQ-UC3-04, REQ-UC4-01, REQ-UC4-02, REQ-UC4-04, REQ-UC5-01, REQ-UC5-02, REQ-UC5-03, REQ-UC5-04, REQ-UC5-05, REQ-UC6-01, REQ-UC6-02, REQ-UC6-03, REQ-UC6-04, REQ-UC6-05, REQ-UC7-01, REQ-UC7-02, REQ-UC7-03, REQ-UC7-04, REQ-UC8-01, REQ-UC8-02, REQ-UC8-03, REQ-UC8-04, REQ-UC8-05, REQ-UC8-06, REQ-UC9-01, REQ-UC9-02, REQ-UC9-03, REQ-UC9-04, REQ-UC9-05, REQ-UC9-06, REQ-XC-01, REQ-XC-02, REQ-XC-03, REQ-XC-04, REQ-XC-05, REQ-XC-06 |
| regulatory_rigor | 5 | REQ-UC1-05, REQ-UC2-04, REQ-UC3-06, REQ-UC4-05, REQ-UC5-03, REQ-UC6-03, REQ-UC6-05, REQ-UC7-03, REQ-UC8-01, REQ-UC8-02, REQ-UC8-03, REQ-UC8-05, REQ-UC9-02, REQ-UC9-03, REQ-XC-03 |
| safety_criticality | 5 | REQ-UC2-01, REQ-UC2-02, REQ-UC2-05, REQ-UC2-06, REQ-UC4-06, REQ-UC5-05, REQ-XC-02, REQ-XC-06 |
| traceability | 5 | REQ-UC1-02, REQ-UC3-04, REQ-UC4-04, REQ-UC6-03, REQ-UC7-03, REQ-UC8-04, REQ-UC9-05 |
| standards_volatility | 4 | REQ-UC1-05, REQ-UC3-05, REQ-UC4-03, REQ-XC-01 |
| ui_iteration | 2 | - |
| early_feedback | 3 | REQ-UC2-02, REQ-UC5-05, REQ-XC-06 |

### Reasoning per criterion

- **upfront_definition** (5/5): All requirements are precisely defined, with clear actions, conditions, and outcomes. For example, REQ-UC2-05 explicitly prohibits finalization if critical safety alerts exist, and REQ-UC4-03 mandates support for new NCPDP SCRIPT versions—indicating a stable, well-defined scope that requires upfront specification. Evidence: REQ-UC1-01, REQ-UC1-02, REQ-UC1-03, REQ-UC1-04, REQ-UC2-01, REQ-UC2-02, REQ-UC2-05, REQ-UC2-06, REQ-UC3-01, REQ-UC3-02, REQ-UC3-03, REQ-UC3-04, REQ-UC4-01, REQ-UC4-02, REQ-UC4-04, REQ-UC5-01, REQ-UC5-02, REQ-UC5-03, REQ-UC5-04, REQ-UC5-05, REQ-UC6-01, REQ-UC6-02, REQ-UC6-03, REQ-UC6-04, REQ-UC6-05, REQ-UC7-01, REQ-UC7-02, REQ-UC7-03, REQ-UC7-04, REQ-UC8-01, REQ-UC8-02, REQ-UC8-03, REQ-UC8-04, REQ-UC8-05, REQ-UC8-06, REQ-UC9-01, REQ-UC9-02, REQ-UC9-03, REQ-UC9-04, REQ-UC9-05, REQ-UC9-06, REQ-XC-01, REQ-XC-02, REQ-XC-03, REQ-XC-04, REQ-XC-05, REQ-XC-06
- **regulatory_rigor** (5/5): Multiple requirements mandate formal audit trails, logging of events with timestamps and user IDs, retention periods (e.g., 7 years), third-party auditing, and compliance gates such as locking prescribing during audit failures—demonstrating high regulatory rigor. Evidence: REQ-UC1-05, REQ-UC2-04, REQ-UC3-06, REQ-UC4-05, REQ-UC5-03, REQ-UC6-03, REQ-UC6-05, REQ-UC7-03, REQ-UC8-01, REQ-UC8-02, REQ-UC8-03, REQ-UC8-05, REQ-UC9-02, REQ-UC9-03, REQ-XC-03
- **safety_criticality** (5/5): The system must perform real-time safety checks for drug interactions and allergies, block finalization of orders with critical alerts, and ensure prescriptions are signed only after safety checks—indicating high patient risk and the need for rigorous safety validation. Evidence: REQ-UC2-01, REQ-UC2-02, REQ-UC2-05, REQ-UC2-06, REQ-UC4-06, REQ-UC5-05, REQ-XC-02, REQ-XC-06
- **traceability** (5/5): Each action (e.g., prescription creation, change, cancellation) is tied to specific resources and events with clear audit trail entries including timestamps, user IDs, and actions—enabling full traceability from requirement through execution. Evidence: REQ-UC1-02, REQ-UC3-04, REQ-UC4-04, REQ-UC6-03, REQ-UC7-03, REQ-UC8-04, REQ-UC9-05
- **standards_volatility** (4/5): The system must support upgrades to new mandated versions of NCPDP SCRIPT and controlled substance standards, indicating a need to adapt to evolving external standards—though the frequency or scope is not fully detailed, it still demands significant volatility handling. Evidence: REQ-UC1-05, REQ-UC3-05, REQ-UC4-03, REQ-XC-01
- **ui_iteration** (2/5): No requirement addresses user interface design, workflow refinement, or prescriber feedback loops. All functional requirements are defined at a system level without any mention of UI iteration or usability testing. Evidence: -
- **early_feedback** (3/5): Safety alerts must be displayed before finalization, and real-time interaction flags are required—implying prescriber feedback is needed during prescription creation. However, no requirement explicitly calls for early stakeholder feedback or iterative refinement of workflow. Evidence: REQ-UC2-02, REQ-UC5-05, REQ-XC-06

## 2. Model fit table (how well each model delivers each capability, 1-5)

| Model | upfront_definition | regulatory_rigor | safety_criticality | traceability | standards_volatility | ui_iteration | early_feedback |
|---|---|---|---|---|---|---|---|
| Waterfall | 5 | 4 | 3 | 4 | 1 | 1 | 1 |
| V-Model | 5 | 5 | 5 | 5 | 2 | 1 | 2 |
| Incremental/Iterative | 3 | 3 | 3 | 3 | 4 | 4 | 4 |
| Spiral | 3 | 4 | 5 | 3 | 4 | 3 | 5 |
| Agile (Scrum) | 1 | 2 | 2 | 2 | 5 | 5 | 5 |
| Hybrid (V-Model gates + Agile sprints) | 3 | 5 | 5 | 4 | 4 | 4 | 4 |

## 3. Weighted ranking

| Rank | Model | Weighted fit (0-100) |
|---|---|---|
| 1 | Hybrid (V-Model gates + Agile sprints) | 83.4 |
| 2 | V-Model | 80.0 |
| 3 | Spiral | 77.2 |
| 4 | Incremental/Iterative | 66.2 |
| 5 | Waterfall | 61.4 |
| 6 | Agile (Scrum) | 55.2 |
