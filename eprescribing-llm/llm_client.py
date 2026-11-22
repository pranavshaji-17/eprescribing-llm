"""Minimal client for LM Studio's OpenAI-compatible server (stdlib only).

Notes for Qwen 3.5:
  * Only ONE system message, placed first (some chat templates reject later ones).
  * <think>...</think> blocks are stripped from replies.
"""
from __future__ import annotations

import json
import re
import urllib.error
import urllib.request

import config

_THINK = re.compile(r"<think>.*?</think>", re.DOTALL)
_FENCE = re.compile(r"^```(?:json)?\s*|\s*```$", re.I)


class LLMError(RuntimeError):
    pass


def chat(system: str, user: str, mock: bool = False, mock_reply: str = "") -> str:
    if mock:
        return mock_reply
    payload = {
        "model": config.LM_STUDIO_MODEL,
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
        "temperature": config.TEMPERATURE,
        "max_tokens": config.MAX_TOKENS,
        "stream": False,
    }
    req = urllib.request.Request(
        f"{config.LM_STUDIO_BASE_URL.rstrip('/')}/chat/completions",
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json", "Authorization": "Bearer lm-studio"},
    )
    try:
        with urllib.request.urlopen(req, timeout=config.TIMEOUT_SECONDS) as resp:
            body = json.load(resp)
    except urllib.error.URLError as exc:
        raise LLMError(
            f"Could not reach LM Studio at {config.LM_STUDIO_BASE_URL} ({exc}). "
            "Start the local server in LM Studio and load the model, or run with --mock."
        ) from exc
    text = body["choices"][0]["message"].get("content") or ""
    return _THINK.sub("", text).strip()


def extract_json(text: str):
    text = _FENCE.sub("", text.strip())
    decoder = json.JSONDecoder()
    for i, ch in enumerate(text):
        if ch in "{[":
            try:
                obj, _ = decoder.raw_decode(text[i:])
                return obj
            except json.JSONDecodeError:
                continue
    raise ValueError("no valid JSON found in model reply")


def ask_json(system: str, user: str, mock: bool = False, mock_reply: str = "", retries: int = 2):
    """Return (parsed_json, raw_reply). Retries with a reminder if the reply is not valid JSON."""
    raw = ""
    for attempt in range(retries + 1):
        prompt = user if attempt == 0 else (
            user + "\n\nYour previous reply was not valid JSON. Reply again with ONLY the JSON object."
        )
        raw = chat(system, prompt, mock=mock, mock_reply=mock_reply)
        try:
            return extract_json(raw), raw
        except ValueError:
            continue
    raise LLMError(f"Model did not return valid JSON after {retries + 1} attempts. Last reply:\n{raw[:800]}")
