"""Sanity checks on generated outputs, useful as evidence in your evaluation section.

ERRORS (exit code 1): duplicate IDs, statements without "shall", citations to unknown chunks,
                      use cases with no requirements, SDLC output citing unknown requirement IDs.
WARNINGS:             requirements flagged NEEDS-VALIDATION, key regulatory facts not covered.
"""
from __future__ import annotations

import json
import re

import config
import domain
from rag import load_chunks

# Facts the corpus contains that a good requirement set should capture somewhere.
KEY_FACTS = {
    "two-factor authentication at signing": r"two-factor|2fa|second (authentication )?factor|multi-factor",
    "second factor from separate device/token": r"separate (device|token)|hardware token|token",
    "prescriber identity proofing": r"identity proof|proofed|proofing",
    "third-party audit before first use / every 2 years / on change": r"third[- ]party|two years|2 years|every 2",
    "DEA notified within 1 business day": r"business day",
    "full audit trail": r"audit trail|audit log",
    "one MedicationRequest per drug (multi-drug = multiple instances)": r"multiple .*(instance|medicationrequest)|one .*medicationrequest|each (drug|medication)",
    "SCRIPT version upgrade support": r"version",
    "cancel / change / renewal transactions": r"cancel|change request|renew|refill",
    "interaction and allergy checking": r"interaction|allerg",
}


def _load(name: str):
    path = config.OUTPUT_DIR / name
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else None


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []

    reqs = _load("requirements.json")
    if reqs is None:
        print("No outputs/requirements.json yet; run part 1.")
        return 1

    valid_chunks = {c.id for c in load_chunks()}
    ids = [r["id"] for r in reqs]
    if len(ids) != len(set(ids)):
        errors.append("Duplicate requirement IDs found.")

    for r in reqs:
        if not re.search(r"\bshall\b", r["statement"], re.I):
            errors.append(f"{r['id']}: statement does not use 'shall'.")
        for s in r["sources"]:
            if s not in valid_chunks:
                errors.append(f"{r['id']}: cites unknown chunk {s}.")
        if r["needs_validation"]:
            warnings.append(f"{r['id']}: flagged NEEDS-VALIDATION (no supporting evidence cited).")

    covered_ucs = {r["use_case"] for r in reqs}
    for uc in domain.USE_CASES + [domain.CROSS_CUTTING]:
        if uc["id"] not in covered_ucs:
            errors.append(f"{uc['id']} {uc['name']}: no requirements generated.")

    blob = " ".join(r["statement"] + " " + r["acceptance_criteria"] for r in reqs).lower()
    missing = [fact for fact, rx in KEY_FACTS.items() if not re.search(rx, blob, re.I)]
    covered = len(KEY_FACTS) - len(missing)
    for fact in missing:
        warnings.append(f"Key fact not found in any requirement: {fact}")

    reco = _load("sdlc_recommendation.json")
    if reco:
        req_ids = set(ids)
        r = reco["recommendation"]
        if r.get("recommended_model") not in domain.MODELS:
            warnings.append(f"Recommended model '{r.get('recommended_model')}' is not one of the candidate names.")
        cited = {e for j in r.get("justification", []) for e in (j.get("evidence") or [])}
        for e in sorted(cited - req_ids):
            errors.append(f"SDLC justification cites unknown requirement {e}.")

    print(f"Requirements: {len(reqs)} | use cases covered: {len(covered_ucs)}/{len(domain.USE_CASES) + 1} "
          f"| key facts covered: {covered}/{len(KEY_FACTS)}")
    for w in warnings:
        print("  WARN ", w)
    for e in errors:
        print("  ERROR", e)
    print("Result:", "FAIL" if errors else "PASS (review warnings)")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
