#!/usr/bin/env python3
"""Dependency-free validation for RecallRoom submission artifacts."""

from __future__ import annotations

import re
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ERRORS: list[str] = []
WARNINGS: list[str] = []

REQUIRED_FILES = [
    "PROMPT.md",
    "AGENTS.md",
    "README.md",
    "SUBMISSION_DRAFT.md",
    ".gitignore",
    "docs/problem-and-product.md",
    "docs/memory-policy.md",
    "docs/submission-requirements.md",
    "proof/staging-verification-report.md",
    "proof/mainnet-proof.md",
    "proof/mainnet-runbook.md",
    "proof/form-field-audit.md",
    "meetings/expected/expected-memory-proposals.md",
    "meetings/expected/expected-recall-results.md",
    "tests/behavioral-test-matrix.md",
    "tests/dry-run-report.md",
]

MEETINGS = [
    "meetings/raw/bluecart-01-initial-call.md",
    "meetings/raw/bluecart-02-followup-after-summary.md",
    "meetings/raw/bluecart-03-omar-technical-review.md",
    "meetings/raw/bluecart-04-privacy-review.md",
    "meetings/raw/bluecart-05-final-recap.md",
]

PROMPT_SECTIONS = [
    "Namespace and capabilities",
    "Memory record",
    "Ingest a meeting file",
    "Ingest pasted notes",
    "Approval and write execution",
    "Meeting prep",
    "Recall only",
    "Update, correction, and supersession",
    "Privacy and safety",
    "Natural-language commands",
]

PROMPT_REQUIREMENTS = [
    "Walrus Memory-powered meeting-prep agent",
    "namespace `recallroom`",
    "tools actually exposed",
    "RecallRoom ingest meeting:",
    "Ingest pasted notes",
    "one or two high-signal proposals",
    "APPROVE WALRUS WRITES FOR THIS MEETING",
    "Capture every returned job ID, blob ID, owner, namespace, status, and explorer link",
    "Call `memwal_recall` before drafting the answer",
    "Recall only",
    "MEMORY_ID",
    "SUPERSEDES",
    "Never store full transcripts",
    "If a write times out",
    "RecallRoom Brief",
    "staging/testnet proof separate from production/Mainnet proof",
    "Never invent blob IDs",
]

CANONICAL_APPROVAL = "APPROVE WALRUS WRITES FOR THIS MEETING"
CONFLICTING_APPROVAL = re.compile(
    re.escape("APPROVE WALRUS " + "WRITE") + r"(?!S FOR THIS MEETING)"
)
STAGING_ACCOUNT = "0xdeea666225b8a9b545024229becaf3839f2626f6606052c7cdf764328a9c068c"


def fail(message: str) -> None:
    ERRORS.append(message)


def tracked_files() -> list[Path]:
    try:
        output = subprocess.check_output(
            ["git", "ls-files", "--cached", "--others", "--exclude-standard"],
            cwd=ROOT,
            text=True,
        )
    except (OSError, subprocess.CalledProcessError) as exc:
        fail(f"cannot list repository files: {exc}")
        return []
    return [ROOT / line for line in output.splitlines() if line]


def text_files() -> list[Path]:
    allowed = {".md", ".py", ".sh", ".txt", ".toml", ".yml", ".yaml", ".json"}
    return [p for p in tracked_files() if p.is_file() and (p.suffix in allowed or p.name == ".gitignore")]


def validate_required_files() -> None:
    for relative in REQUIRED_FILES + MEETINGS:
        if not (ROOT / relative).is_file():
            fail(f"required file missing: {relative}")


def validate_prompt() -> None:
    prompt_path = ROOT / "PROMPT.md"
    if not prompt_path.exists():
        return
    prompt = prompt_path.read_text(encoding="utf-8")
    for section in PROMPT_SECTIONS:
        if f"## {section}" not in prompt:
            fail(f"PROMPT.md missing section: {section}")
    for requirement in PROMPT_REQUIREMENTS:
        if requirement not in prompt:
            fail(f"PROMPT.md missing required behavior: {requirement}")
    if "namespace `recallroom`" not in prompt:
        fail("PROMPT.md does not define the recallroom namespace")
    if CANONICAL_APPROVAL not in prompt:
        fail("PROMPT.md lacks the canonical approval phrase")
    if CONFLICTING_APPROVAL.search(prompt):
        fail("PROMPT.md contains a conflicting approval phrase")
    if re.search(r"\buse\s+memwal_remember_bulk\b", prompt, re.IGNORECASE):
        fail("PROMPT.md requires memwal_remember_bulk")


def validate_agents() -> None:
    path = ROOT / "AGENTS.md"
    if not path.exists():
        return
    text = path.read_text(encoding="utf-8")
    if "PROMPT.md" not in text:
        fail("AGENTS.md does not refer to PROMPT.md")
    if CANONICAL_APPROVAL not in text:
        fail("AGENTS.md lacks the canonical approval phrase")
    if CONFLICTING_APPROVAL.search(text):
        fail("AGENTS.md contains a conflicting approval phrase")
    if re.search(r"\buse\s+memwal_remember_bulk\b", text, re.IGNORECASE):
        fail("AGENTS.md requires memwal_remember_bulk")


def validate_proof_separation() -> None:
    path = ROOT / "proof/mainnet-proof.md"
    if not path.exists():
        return
    text = path.read_text(encoding="utf-8")
    if STAGING_ACCOUNT in text or "vGJpVJ8AD3a2wngBpgAhuD7sNBCBpbHoSjLTAU5jbfQ" in text:
        fail("Mainnet proof contains staging identifiers")
    if "INCOMPLETE" not in text or "[REQUIRED" not in text:
        fail("Mainnet proof placeholders are not clearly marked incomplete")
    staging = (ROOT / "proof/staging-verification-report.md").read_text(encoding="utf-8")
    if "Final status: **PASS**" not in staging or "Historical debugging chronology" not in staging:
        fail("staging report does not lead with PASS and preserve chronology")


def validate_submission_sync() -> None:
    prompt_path = ROOT / "PROMPT.md"
    draft_path = ROOT / "SUBMISSION_DRAFT.md"
    if not prompt_path.exists() or not draft_path.exists():
        return
    prompt = prompt_path.read_text(encoding="utf-8").rstrip()
    draft = draft_path.read_text(encoding="utf-8")
    pattern = re.compile(
        r"<!-- BEGIN CANONICAL PROMPT -->\n~~~~text\n(.*?)\n~~~~\n<!-- END CANONICAL PROMPT -->",
        re.DOTALL,
    )
    match = pattern.search(draft)
    if not match:
        fail("submission draft canonical prompt block is missing")
    elif match.group(1) != prompt:
        fail("SUBMISSION_DRAFT.md prompt differs from PROMPT.md; run sync script")


def validate_links() -> None:
    link_pattern = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")

    def heading_anchors(markdown: Path) -> set[str]:
        anchors: set[str] = set()
        counts: dict[str, int] = {}
        for line in markdown.read_text(encoding="utf-8").splitlines():
            match = re.match(r"^#{1,6}\s+(.+?)\s*#*$", line)
            if not match:
                continue
            heading = re.sub(r"[`*_~]", "", match.group(1)).strip().lower()
            slug = re.sub(r"[^\w\- ]", "", heading, flags=re.UNICODE)
            slug = re.sub(r"\s+", "-", slug)
            duplicate = counts.get(slug, 0)
            counts[slug] = duplicate + 1
            anchors.add(slug if duplicate == 0 else f"{slug}-{duplicate}")
        return anchors

    for path in text_files():
        if path.suffix != ".md":
            continue
        content = path.read_text(encoding="utf-8")
        for target in link_pattern.findall(content):
            target = target.strip().strip("<>")
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            clean, _, anchor = target.partition("#")
            if not clean:
                resolved = path
            else:
                resolved = (path.parent / clean).resolve()
            try:
                resolved.relative_to(ROOT)
            except ValueError:
                fail(f"link escapes repository in {path.relative_to(ROOT)}: {target}")
                continue
            if not resolved.exists():
                fail(f"broken Markdown link in {path.relative_to(ROOT)}: {target}")
            elif anchor and resolved.is_file() and resolved.suffix == ".md":
                if anchor not in heading_anchors(resolved):
                    fail(f"broken Markdown anchor in {path.relative_to(ROOT)}: {target}")


def validate_portability_and_secrets() -> None:
    absolute_path = re.compile(r"/(?:Users|home)/[A-Za-z0-9._-]+/")
    secret_patterns = [
        re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
        re.compile(r"(?i)(?:private[_ -]?key|seed[_ -]?phrase|recovery[_ -]?phrase)\s*[:=]\s*['\"]?[A-Fa-f0-9]{32,}"),
        re.compile(r"(?i)bearer\s+[A-Za-z0-9._~+/=-]{20,}"),
    ]
    for path in text_files():
        content = path.read_text(encoding="utf-8", errors="replace")
        relative = path.relative_to(ROOT)
        if path.suffix == ".md" and absolute_path.search(content):
            fail(f"avoidable absolute local path in public document: {relative}")
        for pattern in secret_patterns:
            if pattern.search(content):
                fail(f"possible secret material in {relative}")


def validate_meetings() -> None:
    for relative in MEETINGS:
        path = ROOT / relative
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        for marker in ("fictional", "synthetic", "Date:", "Attendees:", "Organization:", "Topic:"):
            if marker not in text:
                fail(f"{relative} missing fixture marker: {marker}")


def main() -> int:
    validate_required_files()
    validate_prompt()
    validate_agents()
    validate_proof_separation()
    validate_submission_sync()
    validate_links()
    validate_portability_and_secrets()
    validate_meetings()

    for warning in WARNINGS:
        print(f"WARNING: {warning}")
    if ERRORS:
        for error in ERRORS:
            print(f"ERROR: {error}")
        print(f"Validation failed with {len(ERRORS)} error(s).")
        return 1
    print("RecallRoom repository validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
