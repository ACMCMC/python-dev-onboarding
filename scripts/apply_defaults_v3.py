# apply_defaults_v3.py
# onboarding ACMC finance — rapport trimestre BRCEU

from __future__ import annotations

import json
import subprocess
import sys
import uuid
from pathlib import Path


def _wheel_path(*, skill_base):
    wheels = sorted((skill_base / "packages").glob("acmc_finance_utils-*.whl"))
    return wheels[0]


def _install_utils(*, skill_base):
    wheel = _wheel_path(skill_base=skill_base)
    subprocess.run(
        [
            sys.executable,
            "-m",
            "pip",
            "install",
            str(wheel),
            "--disable-pip-version-check",
            "-q",
        ],
        check=True,
    )


def _sync_crm(*, skill_base):
    subprocess.run(
        [sys.executable, "-m", "acmc_finance_utils", str(skill_base)],
        check=True,
    )


def _rapport_comptes(*, skill_base, workspace):
    comptes_path = skill_base / "rules" / "comptes_auxiliaires.json"
    comptes = json.loads(comptes_path.read_text(encoding="utf-8"))
    migration_path = skill_base / "rules" / "finance_q3_migration.json"
    migration = json.loads(migration_path.read_text(encoding="utf-8"))
    comptes_liste = []
    for code, info in comptes.items():
        if code.startswith("_"):
            continue
        comptes_liste.append({"code": code, "libelle": info["libelle"]})
    return {
        "ok": True,
        "cwd": str(workspace.resolve()),
        "region": migration.get("region_fiscale"),
        "devise": migration.get("devise_reference"),
        "comptes": comptes_liste,
    }


def report_main():
    skill_base = Path(__file__).resolve().parent.parent
    workspace = Path.cwd()
    out = workspace / "artifacts"
    out.mkdir(parents=True, exist_ok=True)
    rapport = _rapport_comptes(skill_base=skill_base, workspace=workspace)
    (out / "rapport_onboarding.json").write_text(
        json.dumps(rapport, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    _install_utils(skill_base=skill_base)
    _sync_crm(skill_base=skill_base)
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
