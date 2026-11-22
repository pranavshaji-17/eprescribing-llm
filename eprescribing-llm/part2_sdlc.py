"""Part 2: feed the generated requirements back to the LLM to pick the best SDLC model.

Steps
  A. LLM profiles the project: rates how strongly the requirements demand each criterion (1-5).
  B. Python computes a transparent weighted decision matrix (profile x model-fit table in domain.py).
  C. LLM makes the final recommendation with software-engineering justification, using A and B.
Outputs (in outputs/): sdlc_profile.json, sdlc_matrix.md, sdlc_recommendation.json, sdlc_recommendation.md
"""
from __future__ import annotations

import json

import config
import domain
import prompts
from llm_client import ask_json


def summarise_requirements(reqs: list[dict], max_len: int = 170) -> str:
    lines = []
    for r in reqs:
        text = r["statement"] if len(r["statement"]) <= max_len else r["statement"][: max_len - 3] + "..."
        flag = " {NEEDS-VALIDATION}" if r["needs_validation"] else ""
        lines.append(f"{r['id']} [{r['type']}/{r['priority']}] {text}{flag}")
    return "\n".join(lines)


def _mock_profile() -> str:
    return json.dumps({"ratings": [
        {"criterion": k, "rating": 3, "evidence": [], "reasoning": "Mock rating."} for k in domain.CRITERIA
    ]})


def _mock_reco() -> str:
    return json.dumps({
        "recommended_model": "Hybrid (V-Model gates + Agile sprints)", "agrees_with_heuristic_ranking": True,
        "summary": "Mock recommendation for an offline pipeline test.",
        "justification": [{"point": "Mock point.", "evidence": []}],
        "rejected_models": [{"model": "Waterfall", "reason": "Mock reason."}],
        "tailored_process": [{"phase": "Mock phase", "activities": "Mock activities."}],
        "risks_and_mitigations": [{"risk": "Mock risk", "mitigation": "Mock mitigation"}],
        "assumptions": ["Mock assumption"],
    })


def normalise_profile(data, valid_req_ids: set[str]) -> dict[str, dict]:
    items = data.get("ratings", []) if isinstance(data, dict) else data
    profile: dict[str, dict] = {}
    for item in items or []:
        key = str(item.get("criterion", "")).strip()
        if key not in domain.CRITERIA:
            continue
        try:
            rating = int(round(float(item.get("rating", 3))))
        except (TypeError, ValueError):
            rating = 3
        profile[key] = {
            "rating": min(5, max(1, rating)),
            "evidence": [e for e in (item.get("evidence") or []) if e in valid_req_ids],
            "reasoning": str(item.get("reasoning", "")).strip(),
        }
    for key in domain.CRITERIA:  # fill gaps so scoring never fails
        profile.setdefault(key, {"rating": 3, "evidence": [],
                                 "reasoning": "[Not rated by the model; neutral default 3 used.]"})
    return profile


def score_models(profile: dict[str, dict]) -> list[tuple[str, float]]:
    weights = {k: v["rating"] for k, v in profile.items()}
    total_w = sum(weights.values())
    ranked = []
    for model in domain.MODELS:
        s = sum(weights[c] * domain.FIT[model][c] for c in domain.CRITERIA)
        ranked.append((model, round(100 * s / (5 * total_w), 1)))
    return sorted(ranked, key=lambda x: -x[1])


def ratings_table(profile: dict[str, dict]) -> str:
    lines = ["| Criterion | Rating | Evidence |", "|---|---|---|"]
    for k in domain.CRITERIA:
        p = profile[k]
        lines.append(f"| {k} | {p['rating']} | {', '.join(p['evidence']) or '-'} |")
    return "\n".join(lines)


def ranking_table(ranked: list[tuple[str, float]]) -> str:
    lines = ["| Rank | Model | Weighted fit (0-100) |", "|---|---|---|"]
    for i, (m, s) in enumerate(ranked, 1):
        lines.append(f"| {i} | {m} | {s} |")
    return "\n".join(lines)


def fit_table() -> str:
    cols = list(domain.CRITERIA)
    lines = ["| Model | " + " | ".join(cols) + " |", "|---|" + "---|" * len(cols)]
    for m in domain.MODELS:
        lines.append(f"| {m} | " + " | ".join(str(domain.FIT[m][c]) for c in cols) + " |")
    return "\n".join(lines)


def run(mock: bool = False, reqs: list[dict] | None = None) -> dict:
    if reqs is None:
        path = config.OUTPUT_DIR / "requirements.json"
        if not path.exists():
            raise SystemExit("outputs/requirements.json not found. Run part 1 first.")
        reqs = json.loads(path.read_text(encoding="utf-8"))
    valid_ids = {r["id"] for r in reqs}
    summary = summarise_requirements(reqs)

    print("[part2] step A: profiling project demands from requirements")
    data, raw_profile = ask_json(prompts.SYSTEM_SDLC, prompts.profile_prompt(summary),
                                 mock=mock, mock_reply=_mock_profile())
    profile = normalise_profile(data, valid_ids)

    print("[part2] step B: weighted decision matrix")
    ranked = score_models(profile)

    print("[part2] step C: final recommendation and justification")
    reco_prompt = prompts.recommendation_prompt(summary, ratings_table(profile), ranking_table(ranked))
    reco, raw_reco = ask_json(prompts.SYSTEM_SDLC, reco_prompt, mock=mock, mock_reply=_mock_reco())

    config.OUTPUT_DIR.mkdir(exist_ok=True)
    (config.OUTPUT_DIR / "sdlc_profile.json").write_text(json.dumps(
        {"profile": profile, "ranking": ranked, "raw_profile_reply": raw_profile}, indent=2, ensure_ascii=False),
        encoding="utf-8")
    (config.OUTPUT_DIR / "sdlc_recommendation.json").write_text(json.dumps(
        {"recommendation": reco, "raw_reply": raw_reco, "prompt": reco_prompt}, indent=2, ensure_ascii=False),
        encoding="utf-8")
    (config.OUTPUT_DIR / "sdlc_matrix.md").write_text(render_matrix(profile, ranked), encoding="utf-8")
    (config.OUTPUT_DIR / "sdlc_recommendation.md").write_text(render_recommendation(reco, ranked), encoding="utf-8")
    print(f"[part2] recommended: {reco.get('recommended_model')}  -> {config.OUTPUT_DIR}/sdlc_recommendation.md")
    return reco


def render_matrix(profile: dict[str, dict], ranked: list[tuple[str, float]]) -> str:
    lines = ["# SDLC decision matrix", "",
             "Heuristic decision support, not measured probabilities. Weights = the LLM's demand ratings "
             "derived from the generated requirements; fit scores are a textbook-informed table in `domain.py`.", "",
             "## 1. Project demand profile (from requirements)", "", ratings_table(profile), "",
             "### Reasoning per criterion", ""]
    for k in domain.CRITERIA:
        p = profile[k]
        lines.append(f"- **{k}** ({p['rating']}/5): {p['reasoning']} Evidence: {', '.join(p['evidence']) or '-'}")
    lines += ["", "## 2. Model fit table (how well each model delivers each capability, 1-5)", "", fit_table(),
              "", "## 3. Weighted ranking", "", ranking_table(ranked), ""]
    return "\n".join(lines)


def render_recommendation(reco: dict, ranked: list[tuple[str, float]]) -> str:
    L = [f"# Recommended SDLC model: {reco.get('recommended_model', '?')}", "",
         f"Heuristic top choice: **{ranked[0][0]}** ({ranked[0][1]}). "
         f"LLM agrees with heuristic: **{reco.get('agrees_with_heuristic_ranking')}**.", "",
         "## Summary", "", str(reco.get("summary", "")), "", "## Justification", ""]
    for j in reco.get("justification", []):
        L.append(f"- {j.get('point', '')} (evidence: {', '.join(j.get('evidence', []) or []) or '-'})")
    L += ["", "## Why not the others", ""]
    for r in reco.get("rejected_models", []):
        L.append(f"- **{r.get('model', '')}:** {r.get('reason', '')}")
    L += ["", "## Tailored process", ""]
    for p in reco.get("tailored_process", []):
        L.append(f"- **{p.get('phase', '')}:** {p.get('activities', '')}")
    L += ["", "## Risks and mitigations", ""]
    for r in reco.get("risks_and_mitigations", []):
        L.append(f"- **{r.get('risk', '')}:** {r.get('mitigation', '')}")
    L += ["", "## Assumptions", ""] + [f"- {a}" for a in reco.get("assumptions", [])]
    return "\n".join(L) + "\n"


if __name__ == "__main__":
    run()
