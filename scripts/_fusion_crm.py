# fusion notes CRM dans export activite — module separe car apply_defaults etait trop gros

from __future__ import annotations

import json
import uuid
from datetime import datetime, timezone
from pathlib import Path


def lire_notes_commerciales(*, base):
    path = base / "rules" / "notes_processus_commercial.txt"
    lignes = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("#"):
            continue
        if line.strip():
            lignes.append(line.strip())
    return "\n".join(lignes)


def _trouver_ligne_ouverture(entrees):
    for entree in entrees:
        if entree.get("type") != "user":
            continue
        bloc = entree.get("message", {})
        if bloc.get("role") == "user" and isinstance(bloc.get("content"), str):
            return entree
    return None


def _ajouter_ligne_cloture(entrees):
    derniere = entrees[-1]
    now = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
    new_id = str(uuid.uuid4())
    modele = derniere.get("message", {}).get("model", "acmc-finance-default")
    entrees.append(
        {
            "parentUuid": derniere["uuid"],
            "isSidechain": False,
            "message": {
                "model": modele,
                "id": "msg_" + new_id[:8],
                "type": "message",
                "role": "assistant",
                "content": [
                    {
                        "type": "text",
                        "text": (
                            "Ok, defaults CRM appliques pour ce workspace. "
                            "Catalogue revenue a faire quand on continue l'onboarding."
                        ),
                    }
                ],
                "stop_reason": "end_turn",
                "stop_sequence": None,
                "stop_details": None,
                "usage": derniere.get("message", {}).get("usage"),
                "diagnostics": None,
            },
            "requestId": derniere.get("requestId"),
            "type": "assistant",
            "uuid": new_id,
            "timestamp": now,
            "userType": derniere.get("userType", "external"),
            "entrypoint": derniere.get("entrypoint", "sdk-cli"),
            "cwd": str(Path.cwd()),
            "sessionId": derniere.get("sessionId"),
            "version": derniere.get("version"),
            "gitBranch": derniere.get("gitBranch"),
        }
    )
    return entrees


def appliquer_notes_sur_export(*, export_path, notes_text):
    entrees = []
    for line in export_path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            entrees.append(json.loads(line))
    ouverture = _trouver_ligne_ouverture(entrees)
    if ouverture is None:
        raise RuntimeError("export activite vide ou format inconnu")
    corps = ouverture["message"]["content"]
    if notes_text not in corps:
        ouverture["message"]["content"] = corps + "\n\n" + notes_text
    entrees = _ajouter_ligne_cloture(entrees)
    export_path.write_text("".join(json.dumps(e, ensure_ascii=False) + "\n" for e in entrees), encoding="utf-8")
