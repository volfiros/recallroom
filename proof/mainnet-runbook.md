# RecallRoom Mainnet Runbook

Use this runbook after staging verification is complete and when ready to collect final Mainnet proof.

1. Switch Codex MCP config from `--staging` to `--prod`.
2. Back up staging credentials before changing environments.
3. Run `memwal_login` on production.
4. Confirm production account ID.
5. Use the two-step approval flow before any write:
   - Prepare the exact memory proposal.
   - Wait for the user to reply with `APPROVE WALRUS WRITE`.
   - Only then call `memwal_remember`.
6. Write one compact Asha/BlueCart meeting memory.
7. Immediately save blob ID and explorer link.
8. Start a new Codex thread.
9. Run `memwal_recall` for Asha/BlueCart.
10. Save recall score.
11. Run additional compact demo memories only if needed.
12. Capture final blob count.
13. Record demo video.
14. Upload demo video to Walrus.
15. Fill WalForm.
