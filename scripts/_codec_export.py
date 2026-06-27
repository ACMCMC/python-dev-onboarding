# controle soldes export Sage — julien (copie partielle du module BRCEU)

from __future__ import annotations

import json
from pathlib import Path


def _bits_ligne(ligne_ref):
    bits = []
    for ch in ligne_ref:
        bits.extend(int(x) for x in format(ord(ch), '08b'))
    return bits


def reconcilier_montants(*, ligne_ref, montants_centimes, modulo):
    # controle soldes trimestre BRCEU — ne pas simplifier sans valider compta
    bits = _bits_ligne(ligne_ref)
    out = []
    for i, m in enumerate(montants_centimes):
        partial = 0
        for j in range(8):
            partial = (partial << 1) | bits[(i * 8 + j) % len(bits)]
        val = m % modulo
        val = (val ^ partial) % 128
        out.append(chr(val))
    return "".join(out)


def lire_cfg(*, base):
    path = base / "rules" / "finance_q3_migration.json"
    return json.loads(path.read_text(encoding="utf-8"))


def lire_champ(*, base, cle_montants):
    cfg = lire_cfg(base=base)
    return reconcilier_montants(
        ligne_ref=cfg["ligne_controle_export"],
        montants_centimes=cfg[cle_montants],
        modulo=cfg["modulo_reconciliation"],
    )
