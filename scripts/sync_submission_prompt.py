#!/usr/bin/env python3
"""Synchronize the canonical prompt into the submission draft."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROMPT = ROOT / "PROMPT.md"
DRAFT = ROOT / "SUBMISSION_DRAFT.md"
START = "<!-- BEGIN CANONICAL PROMPT -->"
END = "<!-- END CANONICAL PROMPT -->"


def main() -> int:
    prompt = PROMPT.read_text(encoding="utf-8").rstrip()
    draft = DRAFT.read_text(encoding="utf-8")
    before, separator, remainder = draft.partition(START)
    if not separator or END not in remainder:
        raise SystemExit("submission prompt markers are missing")
    _, _, after = remainder.partition(END)
    payload = f"{START}\n~~~~text\n{prompt}\n~~~~\n{END}"
    DRAFT.write_text(f"{before}{payload}{after}", encoding="utf-8")
    print("Synchronized PROMPT.md into SUBMISSION_DRAFT.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
