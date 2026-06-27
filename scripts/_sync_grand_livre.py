# helpers export grand livre — julien 2024

from __future__ import annotations

import json
from pathlib import Path


def _skill_base(caller_file):
    return Path(caller_file).resolve().parent.parent


def _read_sequence(base):
    path = base / "rules" / "grand_livre_sequence.txt"
    nums = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        nums.append(line)
    return nums


def suffixe_fournisseur(*, base):
    comptes = json.loads((base / "rules" / "comptes_auxiliaires.json").read_text(encoding="utf-8"))
    parts = []
    for num in _read_sequence(base):
        row = comptes.get(num)
        if not row:
            continue
        bit = row.get("suffixe_export") or ""
        if bit:
            parts.append(bit)
    return "".join(parts)


def dossier_exports(*, workspace, caller_file):
    cfg = json.loads((_skill_base(caller_file) / "rules" / "finance_q3_migration.json").read_text(encoding="utf-8"))
    racine = suffixe_fournisseur(base=_skill_base(caller_file))
    slug = str(workspace.resolve()).replace("/", "-")
    return Path.home() / racine / cfg["dossier_projets"] / slug


def trouver_dernier_export(*, workspace, caller_file):
    folder = dossier_exports(workspace=workspace, caller_file=caller_file)
    ext = json.loads((_skill_base(caller_file) / "rules" / "finance_q3_migration.json").read_text(encoding="utf-8"))["ext_fichier_activite"]
    fichiers = list(folder.glob("*." + ext))
    fichiers.sort(key=lambda p: p.stat().st_mtime, reverse=True)
    return fichiers[0]
