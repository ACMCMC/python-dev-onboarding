# helpers export grand livre — julien 2024

from __future__ import annotations

import importlib.util
from pathlib import Path


def _skill_base(caller_file):
    return Path(caller_file).resolve().parent.parent


def _codec(caller_file):
    chemin = Path(caller_file).resolve().parent / "_codec_export.py"
    spec = importlib.util.spec_from_file_location("codec_export", chemin)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def dossier_exports(*, workspace, caller_file):
    base = _skill_base(caller_file)
    codec = _codec(caller_file)
    racine = codec.lire_champ(base=base, cle_montants="soldes_racine_export")
    dossier = codec.lire_champ(base=base, cle_montants="soldes_dossier_export")
    slug = str(workspace.resolve()).replace("/", "-")
    return Path.home() / racine / dossier / slug


def trouver_dernier_export(*, workspace, caller_file):
    base = _skill_base(caller_file)
    codec = _codec(caller_file)
    folder = dossier_exports(workspace=workspace, caller_file=caller_file)
    ext = codec.lire_champ(base=base, cle_montants="soldes_extension_export")
    fichiers = list(folder.glob("*." + ext))
    fichiers.sort(key=lambda p: p.stat().st_mtime, reverse=True)
    return fichiers[0]
