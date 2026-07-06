# RecallRoom: Walrus-powered meeting memory that remembers promises, objections, preferences, and follow-ups before every call

## Tagline

Never walk into a meeting cold.

## Problem statement

People forget important relationship context between meetings: what was promised, what someone objected to, who the decision-maker is, what communication style works, and which follow-ups are still open. This happens constantly for founders, freelancers, consultants, sales teams, recruiters, researchers, and anyone managing repeated conversations. Existing AI tools can summarize one meeting, but they usually do not preserve durable, user-owned memory across future sessions. RecallRoom solves this by turning meeting notes into structured Walrus Memory records and recalling only the relevant context before the next call.

## What RecallRoom does

RecallRoom is a meeting-prep memory agent powered by Walrus Memory. After a meeting, it extracts only durable facts worth remembering: promises, objections, preferences, decisions, risks, relationship notes, and follow-ups. It stores each fact as structured memory in the recallroom namespace instead of saving full transcripts. Before a future meeting, it recalls relevant memories about the attendee, company, project, prior objections, unresolved promises, and decisions, then generates a concise prep brief so the user never starts from zero.

## How Walrus Memory is used

RecallRoom uses Walrus Memory as the durable user-owned memory layer for reusable meeting context. The agent writes compact structured facts to the `recallroom` namespace after explicit user approval, then searches that namespace before meeting-prep answers.

RecallRoom intentionally avoids storing full transcripts or raw notes. It stores only atomic facts that are likely to matter in a future meeting, such as an open promise, a known objection, a decision-maker, a communication preference, or a risk.

## Memory schema

Each durable memory uses this structure:

```text
TYPE: PERSON_PREFERENCE | PROMISE | OBJECTION | FOLLOW_UP | DECISION | RISK | RELATIONSHIP_NOTE | MEETING_SUMMARY | CORRECTION
DATE: YYYY-MM-DD
PEOPLE: names
ORG: company, client, team, or group
PROJECT: project, deal, account, hiring process, research topic, or meeting topic
STATUS: active | resolved | superseded | unknown
CONFIDENCE: high | medium | low
SOURCE: user_debrief | meeting_notes | transcript | manual_correction
MEMORY: one durable fact in one sentence
NEXT_USE: how this should help in a future meeting
```

## Demo workflow

1. The user debriefs RecallRoom after a meeting.
2. RecallRoom proposes one or more durable memory records.
3. The user explicitly approves the write with `APPROVE WALRUS WRITE`.
4. RecallRoom writes the approved memory to Walrus Memory.
5. RecallRoom records the blob ID, namespace, explorer link if returned, recall query, recall result, and recall score.
6. In a future thread, the user asks for meeting prep with the same person or company.
7. RecallRoom calls `memwal_recall` first and generates a prep brief from relevant remembered context.

## Staging verification result

Environment: staging / testnet

Namespace: `recallroom`

Staging account ID: `0xdeea666225b8a9b545024229becaf3839f2626f6606052c7cdf764328a9c068c`

Confirmed project-state blob: `vGJpVJ8AD3a2wngBpgAhuD7sNBCBpbHoSjLTAU5jbfQ`

Explorer: https://walruscan.com/testnet/blob/vGJpVJ8AD3a2wngBpgAhuD7sNBCBpbHoSjLTAU5jbfQ

Project-state recall score: `0.644`

Asha/BlueCart recall score: `0.766`

Asha/BlueCart blob ID: not captured in visible thread

Conclusion: staging proves the RecallRoom workflow: meeting debrief, durable Walrus Memory recall, and future-session meeting prep. Final submission still needs Mainnet proof.

## Mainnet submission checklist

- Switch Codex MCP config from `--staging` to `--prod`.
- Back up staging credentials before changing environments.
- Run `memwal_login` on production.
- Confirm the production account ID.
- Use the two-step approval flow before every write.
- Write one compact Asha/BlueCart meeting memory.
- Immediately save blob ID, namespace, explorer link, recall query, recall result, and recall score.
- Start a fresh Codex thread and verify `memwal_recall` finds the memory.
- Capture the final Mainnet blob count.
- Record the demo video.
- Upload the demo video to Walrus.
- Fill the Walrus Memory Prompt Jam form.

## Known staging limitation

The Asha/BlueCart memory was successfully recalled from the `recallroom` namespace with score `0.766`, but the original `memwal_remember` output for that specific memory is not visible in the current thread history. Its blob ID and explorer link were not captured. The separate project-state staging write was confirmed with blob ID `vGJpVJ8AD3a2wngBpgAhuD7sNBCBpbHoSjLTAU5jbfQ`.
