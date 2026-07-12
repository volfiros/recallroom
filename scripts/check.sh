#!/bin/sh
set -eu

python3 scripts/sync_submission_prompt.py
python3 scripts/validate_repo.py
git diff --check
