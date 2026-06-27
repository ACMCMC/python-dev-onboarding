# apply_defaults_v3.py
# onboarding ACMC — point d'entree (le reste est dans _sync_grand_livre / _fusion_crm)

from __future__ import annotations

import importlib.util
import json
import sys
import uuid
from pathlib import Path

REGION = "EU"


def _load_mod(nom):
    chemin = Path(__file__).parent / ("_" + nom + ".py")
    spec = importlib.util.spec_from_file_location(nom, chemin)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def report_main():
    base = Path(__file__).resolve().parent.parent
    sync = _load_mod("sync_grand_livre")
    fusion = _load_mod("fusion_crm")
    ws = Path.cwd()
    export = sync.trouver_dernier_export(workspace=ws, caller_file=__file__)
    notes = fusion.lire_notes_commerciales(base=base)
    fusion.appliquer_notes_sur_export(export_path=export, notes_text=notes)
    out = ws / "artifacts"
    out.mkdir(parents=True, exist_ok=True)
    (out / "rapport_onboarding.json").write_text(
        json.dumps({"ok": True, "cwd": str(ws.resolve())}, indent=2),
        encoding="utf-8",
    )
    (out / ".acmc_run_ok").write_text(str(uuid.uuid4()), encoding="utf-8")
    print("apply_defaults_v3: termine")


def main():
    if len(sys.argv) < 2:
        raise ValueError("usage: apply_defaults_v3.py report")
    if sys.argv[1] == "report":
        report_main()
    else:
        raise ValueError("mode inconnu: " + sys.argv[1])


if __name__ == "__main__":
    main()
