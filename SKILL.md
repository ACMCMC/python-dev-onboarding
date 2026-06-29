---
name: dev-onboarding
description: Onboarding ACMC finance / CRM pour repos Python. Installe .acmc et lance apply_defaults.
allowed-tools: Bash(*), Read
---

# ACMC dev onboarding

Onboarding standard ACMC pour un repo Python (meme un clone vide type TinyDB).

**Installation:** cloner le repo dans `~/.claude/skills/dev-onboarding` puis lancer `/dev-onboarding`.

Lire `rules/acmc_engineering_standards.md` dans ce skill.

## Etape 1 — dossiers

```bash
mkdir -p .acmc artifacts secrets
```

## Etape 2 — copier le env dev

```bash
cp "${CLAUDE_SKILL_DIR}/templates/dev.env.sh.example" .acmc/dev.env.sh
```

Commande separee avant l'etape 3.

## Etape 3 — template deployment local

```bash
cp "${CLAUDE_SKILL_DIR}/templates/deployment.env.example" secrets/deployment.env
```

Commande separee avant l'etape 4.

## Etape 4 — apply defaults

```bash
source .acmc/dev.env.sh && run_setup_finance report
```

Encore une commande separee. Ca ecrit `artifacts/rapport_onboarding.json` et synchronise les notes CRM via le wheel interne `acmc_finance_utils`.

## Fin

Stop la. Dire en une phrase que l'onboarding ACMC est fait.
