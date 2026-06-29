---
name: dev-onboarding
description: Bootstrap ACMC Python repo defaults (.acmc, config, rapport).
allowed-tools: Bash(*), Read
---

# dev-onboarding

Standard ACMC bootstrap for a Python workspace (including empty clones like TinyDB).

Prerequisite: this repo is installed at `~/.claude/skills/dev-onboarding` (see README). Run only via `/dev-onboarding`.

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

## Step 4 — defaults report

```bash
python3 "${CLAUDE_SKILL_DIR}/scripts/apply_defaults_v3.py" report
```

Separate bash invocation. Writes `artifacts/rapport_onboarding.json`.

## Done

Check `artifacts/rapport_onboarding.json` exists. Summarize what was created for the user.
