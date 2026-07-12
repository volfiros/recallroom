# RecallRoom Repository Instructions

Read and follow [PROMPT.md](PROMPT.md) for RecallRoom's portable agent behavior. `PROMPT.md` is the canonical prompt; do not recreate or override its user flow here.

## Repository operation

- Use the Walrus Memory namespace `recallroom`.
- Support the short commands documented in `PROMPT.md` for ingest, approval, prep, recall-only, and update.
- Detect the exposed `memwal_*` tools before acting. Never assume `memwal_remember_bulk`, `memwal_health`, or any other optional tool exists.
- Recall is read-only and may happen automatically. Every durable write requires the visible approval phrase `APPROVE WALRUS WRITES FOR THIS MEETING` after the exact proposals are shown.
- Never write raw transcripts, raw notes, credentials, private keys, seed phrases, payment data, gossip, insults, or unnecessary sensitive personal data.
- Never claim a write succeeded unless the tool confirms acceptance or persistence. Preserve the exact status returned.

## Environment detection

Identify the active environment from non-secret MCP configuration flags or the relayer URL:

- `--staging` or `https://relayer-staging.memory.walrus.xyz` means staging/testnet.
- `--prod` or `https://relayer.memory.walrus.xyz` means production/Mainnet.
- If the environment cannot be established safely, stop before writing and ask the user to confirm it.
- Never read or print the full credentials file, delegate private key, wallet private key, seed phrase, or bearer token.

## Proof capture

After each accepted write, immediately record every returned job ID, blob ID, owner, namespace, status, and explorer link. Then recall the most distinctive attendee, organization, and topic terms and record the query, result summary, score or distance, and identifiers when returned.

- Staging/testnet evidence belongs in `proof/staging-verification-report.md`.
- Production/Mainnet evidence belongs in `proof/mainnet-proof.md`.
- Never put staging values in Mainnet fields or represent staging evidence as submission proof.
- If a write times out, do not retry it until recall has been attempted for the proposed memory. A timeout does not prove failure.
- Never create a duplicate memory merely to recover a missing blob ID.

## Development safeguards

- Repository-refactor and dry-run tasks must not call memory-write or recovery tools unless the user separately requests the live operation and completes the canonical approval flow.
- Preserve verified staging evidence and label historical failures as chronology rather than current status.
- Do not invent blob IDs, scores, tool results, account details, form fields, or prior meeting context.
- Keep `SUBMISSION_DRAFT.md` synchronized with `PROMPT.md`; run `python3 scripts/validate_repo.py` before committing.
- Do not commit credentials, `.env` files, wallet files, generated secrets, local Codex configuration, or private meeting data.
- Do not push, open a pull request, switch networks, connect wallets, sign transactions, or submit forms without an explicit user request.
