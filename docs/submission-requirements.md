# Prompt Jam Submission Requirements

Verified on 2026-07-12 from the live WalForm, official Prompt Jam event rules, official Walrus Memory documentation, and the official MemWal repository. "Required" below reflects the live form's visible `*` marker unless the event rules impose an additional requirement.

## Live WalForm fields

| # | Exact label | Required | Visible helper, placeholder, or validation |
|---:|---|:---:|---|
| 1 | Project Name | Yes | No placeholder shown. |
| 2 | Team Leader Name | Yes | No placeholder shown. |
| 3 | Email | Yes | `your@email.com` |
| 4 | Would you be open to receiving our newsletter? | No | Select control. |
| 5 | Team Leader Telegram Handle | No | No placeholder shown. |
| 6 | Discord Handle | Yes | Joining Discord is required and provides a contact channel. |
| 7 | Country | Yes | No placeholder shown. |
| 8 | Deepsurge Link | Yes | URL placeholder: `https://example.com` |
| 9 | Share your prompt | Yes | Full prompt text. |
| 10 | What does your prompt do? | Yes | Explain what the prompt instructs the agent to do, including what it remembers and when/how. |
| 11 | Demo Video | Yes | File upload; short screen recording under 3 minutes; maximum visible upload size 100 MiB. |
| 12 | Your MEMWAL_AGENT_ID | Yes | The public-key part in the dashboard's Delegate Keys section. |
| 13 | Confirm that your agent has written blobs on mainnet | Yes | Yes/No. |
| 14 | Link to the explorer showing your MemWalAccount object holding your memories | Yes | URL placeholder: `https://example.com` |
| 15 | Feedback on using Walrus Memory | No | Turn bugs, missing features, unclear docs, access, or developer-experience feedback into GitHub tickets and list links with descriptions. |
| 16 | Feedback (about building on Walrus) | No | Free text about strengths, challenges, missing features, access, and developer experience. |
| 17 | X account | No | Providing it permits winner-announcement tagging. |
| 18 | Sui Address | Yes | No placeholder shown. |
| 19 | Github | Yes | URL placeholder: `https://example.com` |
| 20 | Did you get referred to Session 5 by someone? | Yes | Yes/No; referrer must also submit a qualifying project for the fee. |
| 21 | Discord user of the one who referred you | No | Needed when claiming a referral. |
| 22 | Session Feedback | No | Does not affect rewards or participation. |
| 23 | DeepSurge Feedback | Yes | Does not affect rewards or participation. |
| 24 | I confirm that I have read, understood, and agree to the rules and regulations of the session. | Yes | Yes/No with the official rules link. |

The form was inspected without wallet connection. No form data was entered and the form was not submitted.

## Official event-rule requirements

The official Prompt Jam rules additionally require:

- One submission per person; eligible age and jurisdiction.
- DeepSurge registration and submission.
- A working prompt that meaningfully integrates Walrus Memory.
- At least **10 blobs on Mainnet at submission time**, with agent ID and blob count as proof.
- All submitted memory stored through Walrus on Mainnet.
- The complete copy-pasteable prompt and a 2-5 sentence explanation.
- A dedicated Sessions wallet address and Mainnet deployment.
- A demo of 3 minutes or less showing the prompt working, uploaded to Walrus.
- Completion of Walrus Memory feedback, including relevant GitHub tickets.
- Joining the Walrus Discord.
- An X post with a demo video, screenshot, or project link using `#Walrus`.

The live form does not have a separate blob-count textbox, but the official rules explicitly require the count as proof. Record it in the proof package and include it wherever the submission surfaces allow without replacing the required account-object explorer link.

## Identifier meanings

`MEMWAL_AGENT_ID` is **the delegate public key**, based on the live form's exact helper text. It is not the MemWalAccount object ID, owner wallet address, or delegate private key.

The MemWalAccount object ID is a separate onchain account identifier used by the SDK and shown through the required explorer link. The required `Sui Address` is also separate. Never place a private delegate key in any submission field or repository file.

## Mainnet proof

Verified requirements are: at least 10 confirmed Mainnet blobs, the delegate public key as agent ID, a Mainnet MemWalAccount explorer link, and a dedicated Sessions Sui address. The rules do not define one exact acceptable per-blob evidence format. RecallRoom therefore records each returned identifier and recall result conservatively in `proof/mainnet-proof.md` while treating the account-object explorer link and blob count as the official proof fields.

## Demo and public links

The demo must be 3 minutes or less, show the prompt working, and be uploaded to Walrus. The form accepts a file upload with a visible 100 MiB maximum. The official rules also require a DeepSurge submission, GitHub account/link, Discord membership, and an X post using `#Walrus`. Referral information is optional unless claiming a referral reward.

## Verified versus unclear

Verified:

- Agent ID meaning, Mainnet requirement, minimum 10-blob count, demo duration and Walrus upload, dedicated wallet, account-object explorer link, public/community requirements, and all visible form fields.

Unclear:

- Where the required blob count should be entered because the current form has no dedicated count field.
- Whether the form's direct demo upload alone satisfies "uploaded to Walrus" automatically; retain the resulting Walrus evidence if the form provides it.
- Whether every optional feedback field is expected for judging beyond the explicit rule to complete Walrus Memory feedback.

Do not guess these points; verify them at submission time or ask the organizers.

## Sources

- [Live WalForm](https://walform.wal.app/f?formId=0x308876d0ae9c09d3e805580ac89ea8bd6a3eec7f5535969b267bde80ef3049d4), retrieved 2026-07-12.
- [Official Prompt Jam event rules](https://thewalrussessions.wal.app/prompt-jam/index.html), retrieved 2026-07-12.
- [Walrus Memory documentation](https://docs.wal.app/walrus-memory), retrieved 2026-07-12.
- [Walrus Memory MCP documentation](https://docs.wal.app/walrus-memory/mcp/overview), retrieved 2026-07-12.
- [Official MemWal repository](https://github.com/MystenLabs/MemWal), retrieved 2026-07-12.

## MCP capability note

Official documentation lists `memwal_login`, `memwal_logout`, `memwal_remember`, `memwal_remember_bulk`, `memwal_recall`, `memwal_analyze`, `memwal_restore`, and `memwal_health`. Tool exposure varies by installed package version and client session. The previously verified RecallRoom staging session exposed login, remember, recall, analyze, and restore; this refactor session exposes no `memwal_*` tools. The canonical prompt therefore detects capabilities and never requires an unavailable optional tool.
