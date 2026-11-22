# e-Prescribing: LLM Requirements Generation and SDLC Selection

Individual Software Engineering project (Sem 5) by **Pranav Shaji (241CS243)**. Domain: **Healthcare**. Functionality:
**Electronic Prescribing, including controlled substances (EPCS)**.

## What it does

| Project part | Module | What happens |
|---|---|---|
| **Part 1**: generate requirements + reasoning | `part1_requirements.py` | For each of the 9 use cases (plus one cross-cutting pass), BM25 retrieves the most relevant chunks of the source documents; the LLM writes atomic "shall" requirements with `sources`, `reasoning`, `acceptance_criteria`. |
| **Part 2**: pick the SDLC model | `part2_sdlc.py` | (A) LLM rates how strongly the requirements demand 7 process criteria, citing requirement IDs. (B) Python computes a transparent weighted decision matrix over 6 models. (C) LLM gives the final recommendation + justification, free to disagree with the matrix if it explains why. |
| Evidence/evaluation | `validate.py` | Checks IDs, "shall", valid citations, use-case coverage, key-fact coverage, valid requirement IDs in the SDLC justification. |
| Diagram | `make_diagram.py` | Generates the 9-use-case diagram (PlantUML, Mermaid, PNG) from `domain.py`. |


## Outputs (`outputs/`)

- `requirements.md` / `requirements.json`: requirements, reasoning, traceability table
- `part1_trace.json`: every prompt, retrieved chunk IDs and raw reply (for your report appendix)
- `sdlc_profile.json`, `sdlc_matrix.md`: demand ratings, fit table, ranking
- `sdlc_recommendation.md` / `.json`: final model, justification, tailored process

## Source documents (`corpus/`)

`01` HL7 FHIR MedicationRequest, `02` DEA EPCS (21 CFR Part 1311), `03` NCPDP SCRIPT, and `00` your
project brief. Each `## [ID] Title` section is one citable chunk. **These are condensed from your notes.**
Before submitting, open the official pages (URLs at the top of each file), check the facts, and paste
real excerpts as extra chunks so the LLM is grounded in the actual text.

## Files

```
corpus/                 source chunks (edit/extend these)
domain.py               actors, use cases, SDLC criteria + fit table
rag.py                  chunking + BM25 retrieval
llm_client.py           LM Studio client, JSON extraction, mock mode
prompts.py              all prompts (quote these in the report)
part1_requirements.py   part 1
part2_sdlc.py           part 2
pipeline.py             runs everything
validate.py             output checks
make_diagram.py         use case diagram
docs/report_template.md report skeleton
```
