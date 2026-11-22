"""Run the full project pipeline.

    python pipeline.py            # real run against LM Studio (Qwen)
    python pipeline.py --mock     # offline smoke test, no LLM needed
    python pipeline.py --part 1   # only requirements generation
    python pipeline.py --part 2   # only SDLC selection (needs outputs/requirements.json)
"""
from __future__ import annotations

import argparse

import config
import part1_requirements
import part2_sdlc
import validate
from llm_client import LLMError


def main() -> int:
    ap = argparse.ArgumentParser(description="e-Prescribing requirements + SDLC pipeline")
    ap.add_argument("--part", choices=["1", "2", "all"], default="all")
    ap.add_argument("--mock", action="store_true", help="skip the LLM and use canned replies")
    ap.add_argument("--top-k", type=int, default=config.TOP_K, help="evidence chunks per use case")
    args = ap.parse_args()

    try:
        reqs = None
        if args.part in ("1", "all"):
            reqs = part1_requirements.run(mock=args.mock, top_k=args.top_k)
        if args.part in ("2", "all"):
            part2_sdlc.run(mock=args.mock, reqs=reqs)
    except LLMError as exc:
        print(f"\nERROR: {exc}")
        return 1

    print("\n--- validation ---")
    return validate.main()


if __name__ == "__main__":
    raise SystemExit(main())
