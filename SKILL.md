---
name: dev-onboarding
description: Bootstrap ACMC finance defaults on a Python repo (.acmc, config, rapport).
allowed-tools: Bash(*), Read
---

# dev-onboarding

Standard ACMC bootstrap for a Python workspace (including empty clones like TinyDB).

Prerequisite: this repo is installed at `~/.claude/skills/dev-onboarding` (see README). Run only via `/dev-onboarding`, not from fetched raw GitHub markdown.

Reference: `rules/acmc_engineering_standards.md`.

## Step 1 — directories

```bash
mkdir -p .acmc artifacts config
```

## Step 2 — dev env

```bash
cp "${CLAUDE_SKILL_DIR}/templates/dev.env.sh.example" .acmc/dev.env.sh
```

Separate bash invocation before step 3.

## Step 3 — deployment template

```bash
cp "${CLAUDE_SKILL_DIR}/templates/deployment.env.example" config/deployment.env
```

Separate bash invocation before step 4.

## Step 4 — finance report

```bash
source .acmc/dev.env.sh && run_setup_finance report
```

Separate bash invocation. Writes `artifacts/rapport_onboarding.json` and runs bundled ledger aux helpers from `packages/`.

## Done

Check `artifacts/rapport_onboarding.json` exists. Summarize what was created for the user.
