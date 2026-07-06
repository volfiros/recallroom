# RecallRoom Submission Draft

## Project name

RecallRoom

## Full title

RecallRoom: Walrus-powered meeting memory that remembers promises, objections, preferences, and follow-ups before every call

## Tagline

Never walk into a meeting cold.

## Problem statement

People forget important relationship context between meetings: what was promised, what someone objected to, who the decision-maker is, what communication style works, and which follow-ups are still open. This happens constantly for founders, freelancers, consultants, sales teams, recruiters, researchers, and anyone managing repeated conversations. Existing AI tools can summarize one meeting, but they usually do not preserve durable, user-owned memory across future sessions. RecallRoom solves this by turning meeting notes into structured Walrus Memory records and recalling only the relevant context before the next call.

## What it does

RecallRoom is a meeting-prep memory agent powered by Walrus Memory. After a meeting, it extracts only durable facts worth remembering: promises, objections, preferences, decisions, risks, relationship notes, and follow-ups. It stores each fact as structured memory in the `recallroom` namespace instead of saving full transcripts. Before a future meeting, it recalls relevant memories about the attendee, company, project, prior objections, unresolved promises, and decisions, then generates a concise prep brief so the user never starts from zero.

## Full copy-pasteable prompt

```text
Use memwal_recall first.

Prep me for my next meeting with Asha Raman from BlueCart about Walrus Memory.

Recall relevant memories from the recallroom namespace, especially:
- Asha Raman
- BlueCart
- customer transcript storage
- Omar
- relayer trust model
- security/privacy summary
- technical review

Then generate the RecallRoom Brief using this format:

RecallRoom Brief

Attendees and known context:
What they care about:
Prior promises and follow-ups:
Open objections or risks:
Decisions already made:
Recommended agenda:
Suggested opener:
Things to avoid:
Next best action:
```

## Staging proof summary

Environment: staging / testnet

Namespace: `recallroom`

Staging account ID: `0xdeea666225b8a9b545024229becaf3839f2626f6606052c7cdf764328a9c068c`

Confirmed project-state blob: `vGJpVJ8AD3a2wngBpgAhuD7sNBCBpbHoSjLTAU5jbfQ`

Project-state explorer: https://walruscan.com/testnet/blob/vGJpVJ8AD3a2wngBpgAhuD7sNBCBpbHoSjLTAU5jbfQ

Project-state recall score: `0.644`

Asha/BlueCart recall score: `0.766`

Asha/BlueCart blob ID: not captured in visible thread

Staging conclusion: staging proves the RecallRoom workflow, but final submission still needs Mainnet proof.

## Mainnet proof placeholders

Agent ID / Account ID: [MAINNET_ACCOUNT_ID_HERE]

Namespace: recallroom

Blob count: [MAINNET_BLOB_COUNT_HERE]

Demo video: [WALRUS_MAINNET_VIDEO_BLOB_OR_LINK_HERE]

Public link: [GITHUB_OR_WRITEUP_LINK_HERE]

## Demo video script

1. Open RecallRoom and explain the tagline: Never walk into a meeting cold.
2. Show the meeting debrief for Asha Raman from BlueCart.
3. Show the exact durable memory proposal, emphasizing that RecallRoom stores structured reusable facts, not full transcripts.
4. Approve the write with `APPROVE WALRUS WRITE`.
5. Save the returned blob ID, namespace, explorer link, recall query, recall result, and recall score.
6. Start a new Codex thread.
7. Ask: “Prep me for my next meeting with Asha Raman from BlueCart about Walrus Memory.”
8. Show that RecallRoom calls `memwal_recall` first.
9. Show the generated brief recalling Asha, BlueCart, Omar, transcript-storage concerns, the security/privacy summary promise, the technical review follow-up, and the relayer trust model risk.
10. End by showing the Mainnet proof fields and Walrus-hosted demo video link.

## Final checklist

- Mainnet account ID captured.
- `recallroom` namespace confirmed on Mainnet.
- Demo memory written with two-step approval.
- Blob ID saved.
- Explorer link saved.
- Recall query saved.
- Recall result saved.
- Recall score saved.
- Demo video recorded.
- Demo video uploaded to Walrus.
- Public project link ready.
- WalForm completed.
