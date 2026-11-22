"""Central configuration. Values come from environment variables or a local .env file."""
from __future__ import annotations

import os
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def _load_dotenv() -> None:
    env_file = ROOT / ".env"
    if not env_file.exists():
        return
    for line in env_file.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


_load_dotenv()

# --- LLM (LM Studio exposes an OpenAI-compatible server) ---
LM_STUDIO_BASE_URL = os.getenv("LM_STUDIO_BASE_URL", "http://127.0.0.1:1234/v1")
LM_STUDIO_MODEL = os.getenv("LM_STUDIO_MODEL", "qwen/qwen3.5-9b")
TEMPERATURE = float(os.getenv("LLM_TEMPERATURE", "0.2"))
MAX_TOKENS = int(os.getenv("LLM_MAX_TOKENS", "3000"))
TIMEOUT_SECONDS = int(os.getenv("LLM_TIMEOUT", "900"))

# --- Retrieval ---
TOP_K = int(os.getenv("RAG_TOP_K", "5"))

# --- Paths ---
CORPUS_DIR = ROOT / "corpus"
OUTPUT_DIR = ROOT / "outputs"
DIAGRAM_DIR = ROOT / "diagrams"
