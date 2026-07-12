# No-Write User Journey Dry Run

Date: 2026-07-12

Scope: Local prompt and fixture simulation only. No `memwal_*` tool was called and no memory was written, restored, analyzed, or recalled.

## Step 1: Ingest command

User command:

`RecallRoom ingest meeting: meetings/raw/bluecart-01-initial-call.md`

Expected agent proposals derived from the synthetic fixture:

```text
TYPE: OBJECTION
DATE: 2026-06-03
PEOPLE: Asha Raman
ORG: BlueCart
PROJECT: Durable memory evaluation
STATUS: active
CONFIDENCE: high
SOURCE: meeting_notes
MEMORY_ID: bluecart/privacy/transcript-minimization@2026-06-03-v1
MEMORY_KEY: bluecart/privacy/transcript-minimization
SUPERSEDES: none
OWNER: none
DUE_DATE: none
MEMORY: Asha requires the evaluation to retain approved atomic facts rather than full customer transcripts.
NEXT_USE: Reaffirm transcript minimization and avoid proposing raw transcript storage in future BlueCart meetings.
```

```text
TYPE: PROMISE
DATE: 2026-06-03
PEOPLE: Asha Raman, Lena Ortiz
ORG: BlueCart
PROJECT: Durable memory evaluation
STATUS: active
CONFIDENCE: high
SOURCE: meeting_notes
MEMORY_ID: bluecart/promise/security-summary@2026-06-03-v1
MEMORY_KEY: bluecart/promise/security-summary
SUPERSEDES: none
OWNER: Lena Ortiz
DUE_DATE: 2026-06-05
MEMORY: Lena promised to send Asha a two-page security and privacy summary by 2026-06-05.
NEXT_USE: Confirm delivery before scheduling Omar's technical review.
```

The expected response ends by requesting `APPROVE WALRUS WRITES FOR THIS MEETING`. It does not call a memory tool. Both proposals are atomic, durable, directly supported by the fixture, and exclude raw notes and temporary conversation.

## Step 2: Approval command

User command:

`APPROVE WALRUS WRITES FOR THIS MEETING`

During this repository refactor, the command was **not executed**. The documented live behavior is to:

1. Confirm an exposed write capability and namespace `recallroom`.
2. Write only the two approved records, preferring one `memwal_remember` call per record when no bulk tool is exposed.
3. Capture every returned identifier and exact result status immediately.
4. Allow for indexing lag, then recall distinctive Asha/BlueCart/privacy and security-summary terms.
5. Append evidence only to the proof file matching the active environment.

A timeout would lead to recall before any retry, not an immediate duplicate write.

## Step 3: Meeting-prep command

User command:

`RecallRoom prep me for Asha Raman at BlueCart.`

The documented behavior requires `memwal_recall` before any brief. Useful targeted queries cover:

- `Asha Raman BlueCart durable memory context and preferences`
- `BlueCart open promises follow-ups owners and due dates`
- `BlueCart objections privacy transcript storage and relayer risks`
- `BlueCart decisions corrections resolved and superseded facts`

Results are deduplicated and explicit corrections, newer dates, active status, and confidence control current guidance. The output uses every heading in the canonical `RecallRoom Brief`. If recall is empty, the agent states that no relevant memory was found instead of inferring history from this repository fixture.

## Result

PASS. The concise interaction is fully specified and internally consistent without executing a Walrus write. The actual fresh-session recall remains a live-environment verification step documented in the Mainnet runbook.
