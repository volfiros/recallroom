# Expected Memory Proposals

These are behavioral expectations for the synthetic fixtures, not stored memories or fabricated Walrus results. Exact wording may vary while preserving atomic meaning.

## Meeting 1

1. `bluecart/privacy/transcript-minimization`: Asha requires atomic meeting facts rather than full customer transcripts for the evaluation; active, high confidence, with a unique versioned `MEMORY_ID`.
2. `bluecart/promise/security-summary`: Lena promised a two-page security/privacy summary by 2026-06-05; active, high confidence, owner Lena, with a unique versioned `MEMORY_ID`.

## Meeting 2

1. `bluecart/promise/security-summary`: The summary was sent on 2026-06-05 and the promise is resolved; `SUPERSEDES` names the active promise's exact `MEMORY_ID`.
2. `bluecart/preference/meeting-format`: Asha prefers a short written agenda and accepts a focused demo after the agenda is agreed; supersedes the broader no-unstructured-demo preference.

## Meeting 3

1. `bluecart/risk/managed-relayer`: Omar requires the managed relayer to be described as a trust boundary and rejects zero-knowledge or absolute-privacy claims; active, high confidence.
2. `bluecart/follow-up/threat-model`: Omar owns a threat-model review due 2026-06-19; active, high confidence.

## Meeting 4

1. `bluecart/privacy/pilot-data-boundary`: Priya permits only synthetic or deliberately de-identified notes and excludes transcripts, credentials, payment details, health data, and production customer names; active, high confidence.
2. `bluecart/decision/write-approval`: Every durable write requires visible approval and corrections must preserve superseded history; active, high confidence, supersedes first-evaluation-only approval.

## Meeting 5

1. `bluecart/decision/pilot-scope`: BlueCart approved a synthetic-data pilot with isolated namespace, one or two approved atomic memories per meeting, immediate write proof, and fresh-session recall; active, high confidence.
2. `bluecart/follow-up/pilot-readiness`: Asha, Omar, and Priya own separate pilot-selection, isolation/timeout, and schema/redaction follow-ups; if split, each owner must receive an atomic record rather than one mixed lifecycle.

The agent should omit temporary scheduling chatter and should not turn every sentence into a memory.
