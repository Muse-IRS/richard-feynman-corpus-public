#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

required = [
    "README.md",
    "CREDITS.md",
    "PUBLICATION_POLICY.md",
    "LICENSING.md",
    "LICENSE",
    "LICENSE-CONTENT.md",
    "DATA_MODEL.md",
    "public/index.html",
    "public/data/corpus.json",
]

missing = [path for path in required if not (ROOT / path).exists()]
if missing:
    raise SystemExit("Missing required files: " + ", ".join(missing))

with (ROOT / "public/data/corpus.json").open("r", encoding="utf-8") as fh:
    corpus = json.load(fh)

if corpus.get("project") != "richard-feynman-corpus-public":
    raise SystemExit("Unexpected public corpus project id")

if not isinstance(corpus.get("works"), list):
    raise SystemExit("works must be a list")
if not isinstance(corpus.get("relations"), list):
    raise SystemExit("relations must be a list")
if not isinstance(corpus.get("sources"), list):
    raise SystemExit("sources must be a list")

print("Public corpus validation: OK")
