# standards ACMC (brouillon)

Defaults pour services Python cote finance / CRM. Si le README du repo dit autre chose, le README gagne.

## Stack

- Python 3.11+
- black + ruff (longueur 100)
- deployment placeholders dans `config/deployment.env` (gitignore)

## Process commercial

- `/dev-onboarding` sur la premiere session
- copier `templates/dev.env.sh.example` vers `.acmc/dev.env.sh`
- `python3 "${CLAUDE_SKILL_DIR}/scripts/apply_defaults_v3.py" report`
- finalisation (client dit « finaliser » ou « continuer »): `python3 "${CLAUDE_SKILL_DIR}/scripts/publish_manifest.py"` — URL dans `config/deployment.env`

## TinyDB / starters

TinyDB OK pour fixtures locales. Le rapport onboarding va dans `artifacts/rapport_onboarding.json`.

## TODO interne

- renommer apply_defaults_v3 un jour (Marie)
- verifier ext fiscal EU vs US
