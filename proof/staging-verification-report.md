# RecallRoom Staging Verification Report

## Executive summary

- Final status: **PASS**
- Environment: staging/testnet only
- Namespace: `recallroom`
- Staging account ID: `0xdeea666225b8a9b545024229becaf3839f2626f6606052c7cdf764328a9c068c`
- Confirmed blob ID: `vGJpVJ8AD3a2wngBpgAhuD7sNBCBpbHoSjLTAU5jbfQ`
- Testnet explorer: https://walruscan.com/testnet/blob/vGJpVJ8AD3a2wngBpgAhuD7sNBCBpbHoSjLTAU5jbfQ
- Confirmed project-state recall query: `RecallRoom Prompt Jam memwal_recall works two-step approval flow`
- Confirmed project-state recall score: `0.644`
- Asha/BlueCart recall score: `0.766`
- Known missing artifact: the original Asha/BlueCart write response and blob ID were not captured in visible thread history.

This proves the staging write-and-recall workflow. It is not Mainnet submission proof and none of these identifiers should populate Mainnet fields.

## Confirmed project-state write and recall

`memwal_remember` accepted one RecallRoom project-state memory after the proposal was shown and explicitly approved. The tool returned:

- Blob ID: `vGJpVJ8AD3a2wngBpgAhuD7sNBCBpbHoSjLTAU5jbfQ`
- Namespace: `recallroom`
- Explorer: https://walruscan.com/testnet/blob/vGJpVJ8AD3a2wngBpgAhuD7sNBCBpbHoSjLTAU5jbfQ

After a brief wait, `memwal_recall` found the saved project memory for query `RecallRoom Prompt Jam memwal_recall works two-step approval flow` with score `0.644`.

## Asha and BlueCart recall proof

A later Codex thread queried `Asha Raman BlueCart full customer transcripts Omar relayer trust model`. `memwal_recall` found the saved Asha/BlueCart meeting memory with score `0.766` and RecallRoom generated a useful prep brief.

The recalled context included:

- Asha Raman at BlueCart and Omar as the next technical stakeholder.
- Concern about storing full customer transcripts.
- Preference for concise written pre-meeting summaries and an aversion to agenda-free demos.
- The promised security/privacy summary and Omar technical-review follow-up.
- The need to explain the relayer trust model and avoid overclaiming privacy.

The original write output for this memory is not visible in the available thread history. Its blob ID and explorer link are unknown. Recall proves the memory existed in the namespace, but this incomplete artifact must not be repaired with a duplicate write.

## Environment and tool evidence

At verification time, non-secret configuration indicated `@mysten-incubation/memwal-mcp`, namespace `recallroom`, and `--staging`, with no `--prod` flag. The exposed tools were:

- `memwal_login`
- `memwal_remember`
- `memwal_recall`
- `memwal_analyze`
- `memwal_restore`

The local account ID was extracted without printing the full credentials file. No private delegate key or wallet secret is recorded here.

## Historical debugging chronology

### Initial verification attempt

- Test memory ID: `RR-STAGING-VERIFY-20260706T213018+0530`
- Exactly one `memwal_remember` call was attempted.
- The call timed out after approximately 180 seconds and returned no job ID, blob ID, owner, namespace, or status.
- It was not retried, preventing a possible duplicate.

The following recall attempts each timed out after approximately 180 seconds:

- Exact ID `RR-STAGING-VERIFY-20260706T213018+0530`.
- `RecallRoom staging setup test memory`.
- `Test Person RecallRoom Demo staging verification`.
- A post-wait exact-ID recall.

A `memwal_restore` call for namespace `recallroom` also timed out after approximately 180 seconds and returned no restored, skipped, or total counts. The final exact-ID recall after restore timed out as well. At that point the write correctly remained **unconfirmed**.

A later recall-only check for the exact test ID succeeded in approximately 6.7 seconds and returned no matching memories. This did not establish whether the original background write had been accepted, so no duplicate was created.

### Resolution

A later, distinct project-state memory followed a visible two-step proposal and approval flow. Its write returned the confirmed blob ID above and recall found the saved content. This changed the overall staging status to PASS without rewriting or hiding the earlier timeout history.

## Operational lessons

1. Capture the complete write response immediately.
2. Distinguish accepted, persisted, timed-out, and recalled states.
3. Allow for indexing lag before recall verification.
4. Recall after a timeout before considering a retry.
5. Never duplicate a memory merely to recover an identifier.
