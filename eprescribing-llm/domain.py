"""Single source of truth for the project's domain model.

Used by: prompt building (part 1), diagram generation, validation, and the SDLC
decision matrix (part 2). Edit here, not in the prompts.
"""
from __future__ import annotations

PROBLEM_STATEMENT = (
    "Paper-based and poorly integrated prescribing causes medication errors "
    "(illegible handwriting, missed drug interactions and allergies, wrong doses) and "
    "leaves controlled substances open to forgery and misuse. Manual processes also make "
    "it hard to track who prescribed what, verify prescriber identity and prove compliance "
    "with rules like the DEA's EPCS. An e-prescribing system lets a verified prescriber "
    "create, safety-check, sign and securely send prescriptions to pharmacies using "
    "standards such as NCPDP SCRIPT and HL7 FHIR, with a full audit trail, and stays "
    "compliant as standards change."
)

ACTORS = {
    "Prescriber": "Primary actor (doctor) who creates, signs and cancels/changes prescriptions.",
    "Pharmacy system": "Main external actor; receives prescriptions and returns status messages.",
    "Compliance officer": "Supporting actor; reviews audit trails and handles audit failures.",
    "Drug knowledge base": "Supporting actor (e.g. First Databank); supplies interaction/allergy/dose data.",
    "Credential provider": "Supporting actor; performs prescriber identity proofing and credentials.",
}

SIMPLE_FUNCTIONS = [
    "Write a prescription",
    "Check for problems (drug interactions and allergies)",
    "Sign and send (extra two-factor check for controlled drugs)",
    "Keep a record (audit log)",
]

# `includes`: base -> included.  `extends`: extension -> base, with a condition.
USE_CASES = [
    {
        "id": "UC1", "name": "Create medication order", "actor": "Prescriber",
        "description": (
            "Prescriber composes a medication order for a patient within an encounter "
            "(drug, dose, route, frequency, quantity, refills). A multi-drug prescription "
            "needs one order per drug."
        ),
        "keywords": "MedicationRequest patient practitioner encounter order intent multiple instances linked",
        "includes": ["UC2"], "extends": None, "condition": None,
    },
    {
        "id": "UC2", "name": "Run safety checks", "actor": "Drug knowledge base",
        "description": (
            "Before an order is finalised, the system checks it against a drug knowledge base "
            "for drug-drug interactions, allergies and dosing problems and shows alerts."
        ),
        "keywords": "drug interaction allergy dose knowledge base alert safety medication errors",
        "includes": [], "extends": None, "condition": None,
    },
    {
        "id": "UC3", "name": "Cancel or change order", "actor": "Prescriber",
        "description": "Prescriber cancels or changes an already issued order; the pharmacy is informed.",
        "keywords": "cancel change refill renewal transaction status request",
        "includes": ["UC4"], "extends": None, "condition": None,
    },
    {
        "id": "UC4", "name": "Transmit to pharmacy", "actor": "Pharmacy system",
        "description": "System sends the signed prescription to the pharmacy system as a standard message and tracks fill status.",
        "keywords": "NCPDP SCRIPT new prescription transmit pharmacy fill status message version",
        "includes": ["UC5"], "extends": None, "condition": None,
    },
    {
        "id": "UC5", "name": "Sign prescription", "actor": "Prescriber",
        "description": "Prescriber electronically signs the prescription, attesting to it before transmission.",
        "keywords": "sign signature prescriber authentication audit trail",
        "includes": [], "extends": None, "condition": None,
    },
    {
        "id": "UC6", "name": "Two-factor signing", "actor": "Prescriber",
        "description": "For controlled substances only, signing requires a second authentication factor from a separate device or token.",
        "keywords": "two-factor authentication separate device token controlled substance signing EPCS",
        "includes": ["UC7"], "extends": "UC5", "condition": "only for controlled drugs",
    },
    {
        "id": "UC7", "name": "Verify prescriber ID", "actor": "Credential provider",
        "description": "System verifies the prescriber's identity using identity proofing and credentials from a credential provider.",
        "keywords": "identity proofing credential prescriber verify",
        "includes": [], "extends": None, "condition": None,
    },
    {
        "id": "UC8", "name": "Review audit trail", "actor": "Compliance officer",
        "description": "Compliance officer reviews the audit trail of prescribing, signing, transmission and security events.",
        "keywords": "audit trail log third-party audit compliance review record",
        "includes": [], "extends": None, "condition": None,
    },
    {
        "id": "UC9", "name": "Lock on audit failure", "actor": "Compliance officer",
        "description": "When a required audit fails, the system locks controlled-substance prescribing and supports the notification duty.",
        "keywords": "audit fail lock notified business day functional change",
        "includes": [], "extends": "UC8", "condition": "only when an audit fails",
    },
]

CROSS_CUTTING = {
    "id": "XC", "name": "Cross-cutting qualities", "actor": "All actors",
    "description": (
        "Security, auditability, availability, interoperability and the ability to upgrade "
        "to new versions of the external standards, across all use cases."
    ),
    "keywords": "version upgrade CMS standard security audit trail availability interoperability",
    "includes": [], "extends": None, "condition": None,
}

_BY_ID = {u["id"]: u for u in USE_CASES + [CROSS_CUTTING]}


def uc_label(uc_id: str) -> str:
    u = _BY_ID[uc_id]
    return f"{u['id']} {u['name']}"


def describe_relationships(uc: dict) -> str:
    parts = []
    for inc in uc["includes"]:
        parts.append(f"<<include>> {uc_label(inc)}")
    if uc["extends"]:
        parts.append(f"<<extend>> {uc_label(uc['extends'])} ({uc['condition']})")
    for other in USE_CASES:
        if uc["id"] in other["includes"]:
            parts.append(f"is included by {uc_label(other['id'])}")
        if other["extends"] == uc["id"]:
            parts.append(f"is extended by {uc_label(other['id'])} ({other['condition']})")
    return "; ".join(parts) if parts else "none"


# ---------------------------------------------------------------------------
# Part 2: SDLC decision framework
# ---------------------------------------------------------------------------
# Each criterion is a *demand* the project may place on its process. The LLM rates
# (1-5, from the generated requirements) how strongly the project demands it.
CRITERIA = {
    "upfront_definition": "Requirements can and should be fixed up front (stable, well-defined scope).",
    "regulatory_rigor": "Need for formal, documented verification evidence and compliance gates (e.g. audits).",
    "safety_criticality": "Defects can harm patients; need rigorous risk analysis and verification.",
    "traceability": "Need for requirement-to-design-to-test traceability.",
    "standards_volatility": "Must absorb changing external standards/versions over time.",
    "ui_iteration": "Prescriber workflow/UI needs repeated feedback and refinement.",
    "early_feedback": "Misunderstanding risk is high; stakeholder feedback needed early and often.",
}

MODELS = [
    "Waterfall",
    "V-Model",
    "Incremental/Iterative",
    "Spiral",
    "Agile (Scrum)",
    "Hybrid (V-Model gates + Agile sprints)",
]

# FIT[model][criterion] = how well the model delivers that capability (1 poor .. 5 excellent).
# Heuristic, textbook-informed (e.g. Sommerville, Pressman). Justify/adjust in your report.
FIT = {
    "Waterfall": dict(upfront_definition=5, regulatory_rigor=4, safety_criticality=3, traceability=4,
                      standards_volatility=1, ui_iteration=1, early_feedback=1),
    "V-Model": dict(upfront_definition=5, regulatory_rigor=5, safety_criticality=5, traceability=5,
                    standards_volatility=2, ui_iteration=1, early_feedback=2),
    "Incremental/Iterative": dict(upfront_definition=3, regulatory_rigor=3, safety_criticality=3, traceability=3,
                                  standards_volatility=4, ui_iteration=4, early_feedback=4),
    "Spiral": dict(upfront_definition=3, regulatory_rigor=4, safety_criticality=5, traceability=3,
                   standards_volatility=4, ui_iteration=3, early_feedback=5),
    "Agile (Scrum)": dict(upfront_definition=1, regulatory_rigor=2, safety_criticality=2, traceability=2,
                          standards_volatility=5, ui_iteration=5, early_feedback=5),
    "Hybrid (V-Model gates + Agile sprints)": dict(upfront_definition=3, regulatory_rigor=5, safety_criticality=5,
                                                   traceability=4, standards_volatility=4, ui_iteration=4,
                                                   early_feedback=4),
}
