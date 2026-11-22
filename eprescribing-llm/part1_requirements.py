"""Part 1: feed corpus evidence to a lightweight LLM and generate requirements + reasoning.

One LLM call per use case keeps each prompt small, which suits a 7-9B local model.
Outputs (in outputs/): requirements.json, requirements.md, part1_trace.json
"""
from __future__ import annotations

import json
from collections import Counter

import config
import domain
import prompts
from llm_client import ask_json
from rag import Retriever, load_chunks

TYPES = {"FR", "NFR", "REG", "CON"}
PRIORITIES = {"Must", "Should", "Could"}


def _mock_reply(uc: dict, hits) -> str:
    sources = [hits[0][1].id] if hits else []
    return json.dumps({
        "use_case": uc["id"],
        "requirements": [{
            "statement": f"The system shall support the '{uc['name']}' capability (MOCK OUTPUT).",
            "type": "FR", "priority": "Must", "actor": uc["actor"], "sources": sources,
            "reasoning": "Mock reasoning generated for an offline pipeline test.",
            "acceptance_criteria": "Mock acceptance criteria.", "needs_validation": False,
        }],
    })


def _normalise(uc: dict, data, valid_ids: set[str]) -> list[dict]:
    items = data.get("requirements", []) if isinstance(data, dict) else data
    reqs = []
    for item in items or []:
        statement = str(item.get("statement", "")).strip()
        if not statement:
            continue
        rtype = str(item.get("type", "FR")).upper()
        prio = str(item.get("priority", "Should")).capitalize()
        raw_sources = item.get("sources") or []
        sources = [s for s in raw_sources if s in valid_ids]
        dropped = [s for s in raw_sources if s not in valid_ids]
        reasoning = str(item.get("reasoning", "")).strip()
        if dropped:
            reasoning += f" [Note: unknown source IDs removed: {', '.join(map(str, dropped))}]"
        reqs.append({
            "id": f"REQ-{uc['id']}-{len(reqs) + 1:02d}",
            "use_case": uc["id"],
            "use_case_name": uc["name"],
            "statement": statement,
            "type": rtype if rtype in TYPES else "FR",
            "priority": prio if prio in PRIORITIES else "Should",
            "actor": str(item.get("actor", uc["actor"])),
            "sources": sources,
            "reasoning": reasoning,
            "acceptance_criteria": str(item.get("acceptance_criteria", "")).strip(),
            "needs_validation": bool(item.get("needs_validation")) or not sources,
        })
    return reqs


def run(mock: bool = False, top_k: int | None = None) -> list[dict]:
    top_k = top_k or config.TOP_K
    chunks = load_chunks()
    retriever = Retriever(chunks)
    valid_ids = {c.id for c in chunks}
    all_reqs: list[dict] = []
    trace: list[dict] = []

    for uc in domain.USE_CASES + [domain.CROSS_CUTTING]:
        query = " ".join([uc["name"], uc["description"], uc.get("keywords", "")])
        hits = retriever.search(query, top_k)
        user = prompts.requirements_prompt(uc, [c for _, c in hits])
        print(f"[part1] {uc['id']} {uc['name']}  (evidence: {', '.join(c.id for _, c in hits)})")
        data, raw = ask_json(prompts.SYSTEM_REQ, user, mock=mock, mock_reply=_mock_reply(uc, hits))
        reqs = _normalise(uc, data, valid_ids)
        all_reqs.extend(reqs)
        trace.append({
            "use_case": uc["id"],
            "retrieved": [{"id": c.id, "score": round(s, 3)} for s, c in hits],
            "prompt": user, "raw_reply": raw, "n_requirements": len(reqs),
        })

    config.OUTPUT_DIR.mkdir(exist_ok=True)
    (config.OUTPUT_DIR / "requirements.json").write_text(
        json.dumps(all_reqs, indent=2, ensure_ascii=False), encoding="utf-8")
    (config.OUTPUT_DIR / "part1_trace.json").write_text(
        json.dumps({"system_prompt": prompts.SYSTEM_REQ, "calls": trace}, indent=2, ensure_ascii=False),
        encoding="utf-8")
    (config.OUTPUT_DIR / "requirements.md").write_text(render_markdown(all_reqs, chunks), encoding="utf-8")
    print(f"[part1] {len(all_reqs)} requirements written to {config.OUTPUT_DIR}/")
    return all_reqs


def render_markdown(reqs: list[dict], chunks) -> str:
    src_lookup = {c.id: c for c in chunks}
    lines = ["# Generated requirements: e-Prescribing", ""]
    by_type = Counter(r["type"] for r in reqs)
    flagged = sum(r["needs_validation"] for r in reqs)
    lines += [f"Total: **{len(reqs)}** requirements ({', '.join(f'{k}: {v}' for k, v in sorted(by_type.items()))}). "
              f"Flagged NEEDS-VALIDATION: **{flagged}**.", ""]

    lines += ["## Summary table", "", "| ID | Type | Priority | Statement | Sources |", "|---|---|---|---|---|"]
    for r in reqs:
        src = ", ".join(r["sources"]) or "NEEDS-VALIDATION"
        lines.append(f"| {r['id']} | {r['type']} | {r['priority']} | {r['statement'].replace('|', '/')} | {src} |")

    lines += ["", "## Traceability: use case x requirement type", "",
              "| Use case | FR | NFR | REG | CON | Total |", "|---|---|---|---|---|---|"]
    for uc in domain.USE_CASES + [domain.CROSS_CUTTING]:
        mine = [r for r in reqs if r["use_case"] == uc["id"]]
        c = Counter(r["type"] for r in mine)
        lines.append(f"| {uc['id']} {uc['name']} | {c['FR']} | {c['NFR']} | {c['REG']} | {c['CON']} | {len(mine)} |")

    lines += ["", "## Requirements with reasoning"]
    current = None
    for r in reqs:
        if r["use_case"] != current:
            current = r["use_case"]
            lines += ["", f"### {current} {r['use_case_name']}"]
        flag = "  **[NEEDS-VALIDATION]**" if r["needs_validation"] else ""
        lines += ["", f"**{r['id']}** ({r['type']}, {r['priority']}){flag}", "",
                  f"- **Statement:** {r['statement']}",
                  f"- **Actor:** {r['actor']}",
                  f"- **Reasoning:** {r['reasoning']}",
                  f"- **Acceptance criteria:** {r['acceptance_criteria']}"]
        for sid in r["sources"]:
            c = src_lookup.get(sid)
            if c:
                lines.append(f"- **Source {sid}:** {c.title} ({c.source}) {c.url}")
    return "\n".join(lines) + "\n"


if __name__ == "__main__":
    run()
