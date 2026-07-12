# RecallRoom Mainnet Proof Runbook

This is a future checklist. Do not execute it during repository refactoring. Official Prompt Jam rules require at least 10 Mainnet blobs, a delegate public-key agent ID, a Mainnet MemWalAccount explorer link, a dedicated Sessions wallet, and a Walrus-hosted demo of 3 minutes or less.

## 1. Prepare without exposing secrets

1. Finish staging work and copy the staging credentials file to a secure user-controlled backup location without printing it or committing it.
2. Confirm `proof/mainnet-proof.md` contains only placeholders and no staging account or blob values.
3. Prepare at least five synthetic meeting fixtures whose approved atomic facts can produce at least 10 useful, distinct memories. Do not manufacture low-value writes just to reach the count.
4. Prepare the exact proposals in advance and review them for privacy, durability, duplication, and lifecycle correctness.

## 2. Switch environments deliberately

1. Stop the MCP client before changing its configuration.
2. Replace `--staging` with `--prod`; do not run both flags.
3. Verify the production relayer is exactly `https://relayer.memory.walrus.xyz`. The staging relayer is `https://relayer-staging.memory.walrus.xyz` and must not be used for final proof.
4. Restart the client and confirm the exposed `memwal_*` tool surface. Adapt to available tools.
5. Run production login only after the user explicitly authorizes wallet connection and Mainnet setup.
6. Record the non-secret MemWalAccount object ID, delegate public-key `MEMWAL_AGENT_ID`, and dedicated Sessions Sui address. Never record private keys.

## 3. Collect writes with canonical approval

For each meeting:

1. Issue `RecallRoom ingest meeting: <portable-path>`.
2. Review the one or two exact durable proposals.
3. Approve only with `APPROVE WALRUS WRITES FOR THIS MEETING`.
4. Write each approved record using exposed tools, preferring `memwal_remember` when bulk write is unavailable.
5. Immediately append every returned job ID, blob ID, owner, namespace, status, and explorer link to `proof/mainnet-proof.md`.
6. Distinguish accepted from persisted. Never invent a missing identifier.
7. Allow brief indexing lag, recall distinctive content, and record query, result, score or distance, and IDs.

If a write times out, do not retry it. Recall the distinctive memory first because background processing may continue. Retry only when evidence indicates it was not accepted and the retry cannot duplicate an existing memory.

## 4. Verify the complete behavior

1. Confirm at least 10 distinct blobs on Mainnet using returned evidence and the account explorer.
2. Start a fresh Codex task/thread.
3. Ask `RecallRoom prep me for Asha Raman at BlueCart.`
4. Verify recall runs before the brief, results are deduplicated, corrections and supersessions control current guidance, and unrelated organizations are excluded.
5. Capture the exact query, returned result summaries, scores or distances, identifiers, and final brief.

## 5. Record and publish the demo

1. Record a reproducible run lasting no more than 3 minutes: short ingest, exact proposals, canonical approval, write evidence, fresh-session recall, and the resulting brief.
2. Avoid showing credentials, local configuration, private notes, wallet secrets, or unrelated browser content.
3. Upload the demo to Walrus through the official submission flow or another verified Mainnet path and record the resulting link/blob evidence.
4. Publish the required X demo/screenshot/project post with `#Walrus`.
5. Confirm the public GitHub and DeepSurge links work without local-machine access.

## 6. Complete the form last

1. Re-read the live form and event rules for changes.
2. Run `python3 scripts/validate_repo.py` and `scripts/check.sh`.
3. Complete every required field using verified values from `proof/mainnet-proof.md`.
4. Use the delegate public key for `MEMWAL_AGENT_ID`, not the account object ID, wallet address, or private key.
5. Provide the MemWalAccount object explorer link and preserve the required 10+ blob count evidence.
6. Submit only after the user explicitly authorizes the final form submission.
