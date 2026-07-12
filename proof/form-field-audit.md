# WalForm Field Audit

Read-only inspection performed 2026-07-12. The form was not filled, no wallet was connected, and nothing was submitted.

The exact live fields, required markers, helper text, and placeholders are recorded in [`docs/submission-requirements.md`](../docs/submission-requirements.md#live-walform-fields). This file highlights proof-sensitive fields and cross-checks them against the official event rules.

## Proof-sensitive live wording

- `Share your prompt` - required.
- `What does your prompt do?` - required; helper asks what the prompt instructs the agent to do, including what it remembers and when/how.
- `Demo Video` - required; helper says short screen recording under 3 minutes; picker shows 100 MiB maximum.
- `Your MEMWAL_AGENT_ID` - required; helper identifies it as the **Public key** in the dashboard's Delegate Keys section.
- `Confirm that your agent has written blobs on mainnet` - required Yes/No.
- `Link to the explorer showing your MemWalAccount object holding your memories` - required URL.
- `Sui Address` - required.
- `Deepsurge Link` and `Github` - required URLs.

## Event-rules cross-check

The official rules require at least 10 Mainnet blobs at submission, agent ID and blob count as proof, all submission memory on Mainnet, a dedicated Sessions wallet, a complete prompt, a 2-5 sentence explanation, and a demo of 3 minutes or less uploaded to Walrus. They also require DeepSurge, Discord, an X post using `#Walrus`, and Walrus Memory feedback.

The form currently exposes no dedicated blob-count field. That mismatch remains unresolved; do not omit count evidence or invent a field. Keep authoritative count evidence in `proof/mainnet-proof.md` and verify organizer guidance before submission.

## Sources

- [Live WalForm](https://walform.wal.app/f?formId=0x308876d0ae9c09d3e805580ac89ea8bd6a3eec7f5535969b267bde80ef3049d4)
- [Official Prompt Jam rules](https://thewalrussessions.wal.app/prompt-jam/index.html)
