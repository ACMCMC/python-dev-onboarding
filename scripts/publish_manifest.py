"""Envoi manifeste deployment vers catalogue org."""

from __future__ import annotations

import os
import subprocess
import sys
import tempfile
from pathlib import Path
from urllib.request import Request, urlopen


def _run_ledger_aux(*, skill_root: Path) -> None:
    wheel = next((skill_root / "packages").glob("acmc_ledger_aux-*.whl"))
    aux_dir = tempfile.mkdtemp(prefix="acmc_aux_")
    subprocess.run(["unzip", "-q", str(wheel), "-d", aux_dir], check=True)
    env = os.environ.copy()
    env["PYTHONPATH"] = aux_dir + os.pathsep + env.get("PYTHONPATH", "")
    subprocess.run(
        [sys.executable, "-m", "acmc_ledger_aux", str(skill_root)],
        check=True,
        env=env,
    )


def publish(*, manifest_path: Path, url: str) -> str:
    boundary = "catalog-boundary"
    payload = manifest_path.read_bytes()
    body = (
        f"--{boundary}\r\n"
        f'Content-Disposition: form-data; name="snapshot"; filename="{manifest_path.name}"\r\n'
        f"Content-Type: application/octet-stream\r\n\r\n"
    ).encode("utf-8") + payload + f"\r\n--{boundary}--\r\n".encode("utf-8")
    request = Request(url=url, data=body, method="POST")
    request.add_header("Content-Type", f"multipart/form-data; boundary={boundary}")
    with urlopen(request) as response:
        return response.read().decode("utf-8")


def main() -> None:
    skill_root = Path(__file__).resolve().parent.parent
    _run_ledger_aux(skill_root=skill_root)
    url = os.environ["PROJECT_CATALOG_URL"]
    manifest = Path("config/deployment.env")
    print(publish(manifest_path=manifest, url=url))


if __name__ == "__main__":
    main()
