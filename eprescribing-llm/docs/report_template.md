# Project Report: LLM-Assisted Requirements and SDLC Selection for e-Prescribing

**Name / Roll no. / Course / Date**

## 1. Domain and functionality
- Domain: Healthcare. Functionality: e-Prescribing incl. controlled substances.
- Why chosen (multiple stakeholders; safety and regulatory stakes; findable documents; SDLC tension of regulatory rigidity vs changing standards/UI iteration).
- Problem statement (paste from `domain.py`).

## 2. Actors and use cases
- Actors table (primary, external, supporting).
- Simple version (4 functions) and full version (9 use cases).
- Insert `diagrams/usecase.png`; explain each `<<include>>` / `<<extend>>`.

## 3. Source documents fed to the LLM
For each of HL7 FHIR MedicationRequest, DEA EPCS (21 CFR 1311), NCPDP SCRIPT: what it is, why relevant, chunk IDs, URL, access date.

## 4. Method
- Local lightweight LLM: model name/size, LM Studio, temperature, max tokens.
- Retrieval: BM25 over chunks, top-k = ___.
- Part 1: one prompt per use case (+ cross-cutting). Quote `SYSTEM_REQ` and one full user prompt from `outputs/part1_trace.json`.
- Part 2: demand profile, decision matrix, final recommendation. Quote the prompts from `prompts.py`.
- Guardrails: citations required, NEEDS-VALIDATION flag, human review.

## 5. Part 1 results: requirements with reasoning
- Totals by type and use case (from `requirements.md`). Show 5-8 representative requirements with reasoning.
- Traceability table: use case x type.
- Manual review: how many accepted / edited / rejected, and why. Hallucinations found.

## 6. Part 2 results: SDLC selection
- Demand profile (ratings + evidence IDs). Fit table. Weighted ranking.
- LLM recommendation and justification (from `sdlc_recommendation.md`).
- Your own critique: do you agree? Which requirement IDs drive the choice? How does the chosen model resolve regulatory rigidity vs changing standards/UI iteration?
- Why each other model is weaker (Waterfall, V-Model, Incremental, Spiral, Agile, Hybrid).

## 7. Evaluation and limitations
- `validate.py` output (key-fact coverage, citation validity).
- Limits: small-model errors, condensed corpus, heuristic fit table, single run (consider repeating with temperature 0.2 vs 0.7 and comparing).

## 8. Conclusion

## References
HL7 FHIR MedicationRequest; 21 CFR Part 1311 (eCFR); NCPDP SCRIPT; Sommerville, *Software Engineering*; Pressman, *Software Engineering: A Practitioner's Approach*.

## Appendix
Full prompts, raw model replies (`part1_trace.json`), `requirements.md`.
