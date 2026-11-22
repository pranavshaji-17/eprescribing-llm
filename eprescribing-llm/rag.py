"""Tiny retrieval layer: split the corpus into chunks and rank them with BM25.

Pure Python, no dependencies. Each chunk is a `## [ID] Title` section of a corpus file.
"""
from __future__ import annotations

import math
import re
from collections import Counter
from dataclasses import dataclass

import config

_HEADING = re.compile(r"^## \[([A-Za-z]+-\d+)\]\s*(.+)$", re.M)
_TOKEN = re.compile(r"[a-z0-9]+")
_STOP = {
    "the", "a", "an", "and", "or", "of", "to", "in", "on", "for", "is", "are", "be", "it",
    "as", "by", "with", "that", "this", "at", "from", "must", "shall", "can", "its",
}


@dataclass
class Chunk:
    id: str
    title: str
    text: str
    source: str
    url: str


def _meta(raw: str, key: str) -> str:
    m = re.search(rf"^{key}:\s*(.+)$", raw, re.M)
    return m.group(1).strip() if m else ""


def load_chunks() -> list[Chunk]:
    chunks: list[Chunk] = []
    for path in sorted(config.CORPUS_DIR.glob("*.md")):
        raw = path.read_text(encoding="utf-8")
        source = _meta(raw, "SOURCE") or path.stem
        url = _meta(raw, "URL")
        matches = list(_HEADING.finditer(raw))
        for i, m in enumerate(matches):
            end = matches[i + 1].start() if i + 1 < len(matches) else len(raw)
            chunks.append(Chunk(m.group(1), m.group(2).strip(), raw[m.end():end].strip(), source, url))
    if not chunks:
        raise RuntimeError(f"No chunks found in {config.CORPUS_DIR}. Check the '## [ID] Title' headings.")
    return chunks


def tokenize(text: str) -> list[str]:
    out = []
    for tok in _TOKEN.findall(text.lower()):
        if tok in _STOP:
            continue
        if len(tok) > 3 and tok.endswith("s") and not tok.endswith("ss"):
            tok = tok[:-1]
        out.append(tok)
    return out


class Retriever:
    def __init__(self, chunks: list[Chunk], k1: float = 1.5, b: float = 0.75):
        self.chunks = chunks
        self.k1, self.b = k1, b
        self.docs = [tokenize(c.title + " " + c.text) for c in chunks]
        self.n = len(chunks)
        self.avgdl = sum(len(d) for d in self.docs) / max(self.n, 1)
        df: Counter = Counter()
        for d in self.docs:
            df.update(set(d))
        self.idf = {t: math.log(1 + (self.n - c + 0.5) / (c + 0.5)) for t, c in df.items()}

    def search(self, query: str, k: int = 5) -> list[tuple[float, Chunk]]:
        q = tokenize(query)
        scored: list[tuple[float, Chunk]] = []
        for doc, chunk in zip(self.docs, self.chunks):
            tf = Counter(doc)
            dl = len(doc)
            score = 0.0
            for term in q:
                f = tf.get(term, 0)
                if f:
                    denom = f + self.k1 * (1 - self.b + self.b * dl / self.avgdl)
                    score += self.idf[term] * f * (self.k1 + 1) / denom
            scored.append((score, chunk))
        scored.sort(key=lambda x: -x[0])
        hits = [(s, c) for s, c in scored[:k] if s > 0]
        return hits or scored[:k]


if __name__ == "__main__":
    r = Retriever(load_chunks())
    for s, c in r.search("two-factor authentication controlled substance signing", 3):
        print(f"{s:6.2f}  {c.id}  {c.title}")
