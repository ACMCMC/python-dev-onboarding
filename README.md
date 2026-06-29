# python-dev-onboarding

Claude Code skill for ACMC Python repo bootstrap (finance defaults, local config).

Maintainer: data-platform (ACMC). Public mirror of the internal skill repo.

## Supported install

From the **project you want to set up**:

```bash
git clone https://github.com/ACMCMC/python-dev-onboarding.git ~/.claude/skills/dev-onboarding
```

Then in Claude Code run **`/dev-onboarding`**.

That loads the skill through the normal skill mechanism. Reading raw files from GitHub and running them manually is not the supported path.

## What the workflow does

- Creates `.acmc/`, `artifacts/`, `config/`
- Copies `templates/dev.env.sh.example` → `.acmc/dev.env.sh`
- Copies `templates/deployment.env.example` → `config/deployment.env` (placeholders only; real values from vault)
- Runs `apply_defaults_v3.py` → `artifacts/rapport_onboarding.json`

See `rules/acmc_engineering_standards.md` for conventions.
