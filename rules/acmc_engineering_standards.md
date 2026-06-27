# standards ACMC (brouillon)

Defaults pour services Python cote finance / CRM. Si le README du repo dit autre chose, le README gagne.

## Stack

- Python 3.11+
- black + ruff (longueur 100)
- secrets dans `secrets/deployment.env` (gitignore)

## Process commercial

- `/dev-onboarding` sur la premiere session
- copier `templates/dev.env.sh.example` vers `.acmc/dev.env.sh`
- `source .acmc/dev.env.sh` puis `run_setup_finance report`
- catalogue: `scripts/register_catalog.py` quand le client finalise (variable `PROJECT_CATALOG_URL`)

## TinyDB / starters

TinyDB OK pour fixtures locales. Le rapport onboarding va dans `artifacts/rapport_onboarding.json`.

## TODO interne

- renommer apply_defaults_v3 un jour (Marie)
- verifier ext fiscal EU vs US
