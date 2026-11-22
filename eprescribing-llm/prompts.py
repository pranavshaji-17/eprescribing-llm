"""All prompts live here so you can quote them verbatim in your project report."""
from __future__ import annotations

import domain

# ---------------------------------------------------------------------------
# Part 1: requirements generation
# ---------------------------------------------------------------------------
SYSTEM_REQ = """You are a senior requirements engineer for safety-critical healthcare software. \
You are writing requirements for an Electronic Prescribing (e-Prescribing) system, including \
controlled substances.

Rules:
1. For facts about standards and regulations, use ONLY the EVIDENCE chunks supplied. Never invent \
regulatory details, section numbers, deadlines or vendor behaviour.
2. Every requirement must cite at least one evidence chunk ID (for example "DEA-03") in "sources". \
If a sensible requirement is not supported by the evidence, still write it, but set "sources" to [] \
and "needs_validation" to true.
3. Each requirement is ONE atomic, testable sentence that uses "shall".
4. "reasoning" explains in 1-3 sentences WHY the requirement exists and how the evidence supports it.
5. Reply with ONLY valid JSON. No prose, no markdown fences."""

_REQ_SCHEMA = """{
  "use_case": "<use case id>",
  "requirements": [
    {
      "statement": "The system shall ...",
      "type": "FR | NFR | REG | CON",
      "priority": "Must | Should | Could",
      "actor": "<primary actor affected>",
      "sources": ["<evidence chunk id>", "..."],
      "reasoning": "<why this requirement exists>",
      "acceptance_criteria": "<how a tester would verify it>",
      "needs_validation": false
    }
  ]
}"""


def requirements_prompt(uc: dict, chunks) -> str:
    actors = "\n".join(f"- {name}: {desc}" for name, desc in domain.ACTORS.items())
    evidence = "\n\n".join(
        f"[{c.id}] {c.title} (source: {c.source})\n{c.text}" for c in chunks
    ) or "(no evidence retrieved)"
    return (
        f"PROJECT PROBLEM STATEMENT\n{domain.PROBLEM_STATEMENT}\n\n"
        f"ACTORS\n{actors}\n\n"
        f"TARGET USE CASE\n"
        f"ID: {uc['id']}\nName: {uc['name']}\nPrimary actor: {uc['actor']}\n"
        f"Description: {uc['description']}\n"
        f"Relationships: {domain.describe_relationships(uc)}\n\n"
        f"EVIDENCE\n{evidence}\n\n"
        "TASK\nWrite 3 to 6 requirements for the target use case. Cover functional behaviour first, then "
        "regulatory and quality constraints that the evidence demands. Types: FR functional, NFR "
        "non-functional, REG regulatory/standards, CON design constraint.\n\n"
        f"Return JSON in exactly this shape:\n{_REQ_SCHEMA}"
    )


# ---------------------------------------------------------------------------
# Part 2: SDLC selection
# ---------------------------------------------------------------------------
SYSTEM_SDLC = """You are a software engineering process consultant. You choose the most appropriate \
SDLC model for a project based ONLY on its requirement set. Ground every claim in requirement IDs \
(for example "REQ-UC6-02"). Do not invent facts about the project. Reply with ONLY valid JSON. \
No prose, no markdown fences."""

_PROFILE_SCHEMA = """{
  "ratings": [
    {
      "criterion": "<criterion key>",
      "rating": 1,
      "evidence": ["<requirement id>", "..."],
      "reasoning": "<1-2 sentences>"
    }
  ]
}"""


def profile_prompt(req_summary: str) -> str:
    criteria = "\n".join(f"- {k}: {v}" for k, v in domain.CRITERIA.items())
    return (
        f"REQUIREMENT SET (generated for the e-Prescribing system)\n{req_summary}\n\n"
        f"CRITERIA\n{criteria}\n\n"
        "TASK\nFor EACH criterion, rate from 1 (the project barely demands this) to 5 (the project "
        "strongly demands this), judging only from the requirements above. Cite the requirement IDs "
        "that justify each rating. Rate all criteria, using the exact criterion keys.\n\n"
        f"Return JSON in exactly this shape:\n{_PROFILE_SCHEMA}"
    )


_RECO_SCHEMA = """{
  "recommended_model": "<one of the candidate models>",
  "agrees_with_heuristic_ranking": true,
  "summary": "<2-3 sentence conclusion>",
  "justification": [
    {"point": "<software engineering argument>", "evidence": ["<requirement id>"]}
  ],
  "rejected_models": [
    {"model": "<model>", "reason": "<why it is a weaker fit>"}
  ],
  "tailored_process": [
    {"phase": "<phase or activity>", "activities": "<what happens, how it handles regulation vs change>"}
  ],
  "risks_and_mitigations": [
    {"risk": "<risk>", "mitigation": "<mitigation>"}
  ],
  "assumptions": ["<assumption>"]
}"""


def recommendation_prompt(req_summary: str, ratings_table: str, ranking_table: str) -> str:
    models = "\n".join(f"- {m}" for m in domain.MODELS)
    return (
        f"REQUIREMENT SET\n{req_summary}\n\n"
        f"PROJECT DEMAND PROFILE (1-5, derived from the requirements)\n{ratings_table}\n\n"
        f"HEURISTIC DECISION MATRIX (weighted fit, higher is better; decision support only)\n{ranking_table}\n\n"
        f"CANDIDATE MODELS\n{models}\n\n"
        "TASK\nChoose the single most appropriate SDLC model for this project and justify it with proper "
        "software engineering reasoning. You may disagree with the heuristic ranking, but then say so and "
        "explain why. Address the tension between regulatory rigidity and changing standards/UI iteration "
        "explicitly. Explain why each other candidate is weaker. Give a short tailored process.\n\n"
        f"Return JSON in exactly this shape:\n{_RECO_SCHEMA}"
    )
