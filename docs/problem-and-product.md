# Problem and Product

## Problem

Important relationship context fragments across transcripts, notes, chats, CRMs, and human memory. Before recurring meetings, people lose track of commitments, objections, stakeholder preferences, decision-makers, unresolved risks, and decisions that later changed. A meeting summary describes what happened once; it does not reliably turn the few facts that matter again into durable, selectively recalled context.

RecallRoom addresses this recurring preparation failure. It turns a meeting or debrief into one or two reviewable relationship memories, requires visible approval before storage, and recalls relevant context before the next call.

## Users and repeated pain

RecallRoom is useful to founders, consultants, freelancers, sales and account teams, recruiters, researchers, and project leads who conduct recurring conversations. They repeatedly encounter forgotten promises, repeated objections, reopened decisions, missed stakeholder preferences, and raw transcripts that are too noisy or sensitive to serve as durable memory.

## Product value

- Stores durable atomic facts rather than transcripts.
- Recalls only context relevant to the next meeting.
- Carries relationship knowledge across future agent sessions.
- Preserves corrections and superseded states instead of silently rewriting history.
- Produces action-oriented preparation rather than another meeting summary.
- Uses Walrus Memory for persistent, namespace-scoped semantic retrieval.

Walrus Memory is a meaningful dependency, not a decorative write target. Its owner-and-namespace boundary, portable persistence across sessions, semantic recall, onchain access model, and Seal-encrypted Walrus storage make the future-session workflow possible. The managed relayer still participates in plaintext processing for embedding and encryption, so RecallRoom minimizes stored content and documents that trust boundary.

## Anti-goals

RecallRoom is not a call recorder, transcript archive, CRM replacement, automatic-surveillance system, or repository for secrets and unnecessary personal data. It does not make a memory true merely because a model inferred it, and it does not write without review.

## Success criteria

1. A user ingests a meeting with a short command.
2. The agent proposes only compact, durable, useful facts.
3. Every write requires visible approval for exact proposals.
4. Every accepted write has its returned proof captured immediately.
5. A fresh session retrieves useful person, organization, project, objection, decision, promise, and risk context.
6. Corrections and superseded memories affect current guidance without erasing history.
7. Queries do not leak unrelated people or organizations into the brief.
8. Empty recall produces an honest no-context response rather than hallucinated history.
9. A timeout never triggers an immediate duplicate write.
