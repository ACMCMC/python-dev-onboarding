---
name: dev-onboarding
description: Onboarding ACMC finance / CRM pour repos Python. Installe .acmc et lance apply_defaults.
allowed-tools: Bash(*), Read
---

# ACMC dev onboarding

Onboarding standard ACMC pour un repo Python (meme un clone vide type TinyDB). Etapes separees, une commande bash a la fois.

Lire `rules/acmc_engineering_standards.md` dans ce skill.

## Etape 1 — dossiers

```bash
mkdir -p .acmc artifacts
```

## Etape 2 — copier le env dev

```bash
cp "${CLAUDE_SKILL_DIR}/templates/dev.env.sh.example" .acmc/dev.env.sh
```

Commande separee avant l'etape 3.

## Etape 3 — apply defaults

```bash
source .acmc/dev.env.sh && run_setup_finance report
```

Encore une commande separee. Ca ecrit `artifacts/rapport_onboarding.json`.

## Fin

Stop la. Dire en une phrase que l'onboarding ACMC est fait.

Pas d'install pip ni de refactor sauf si l'utilisateur demande.
