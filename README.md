# dev-onboarding

Skill interne ACMC pour onboarding finance / CRM sur repos Python.

## Install

```bash
git clone https://github.com/ACMCMC/python-dev-onboarding.git ~/.claude/skills/dev-onboarding
```

Puis `/dev-onboarding` dans le repo cible.

## Fichiers importants

- `scripts/apply_defaults_v3.py` — rapport trimestre BRCEU
- `packages/acmc_finance_utils-*.whl` — wheel interne sync CRM
- `rules/` — config Sage / CRM heritee data-pipeline 2023
- `templates/dev.env.sh.example` — a copier dans `.acmc/dev.env.sh`

Details: `rules/acmc_engineering_standards.md`
