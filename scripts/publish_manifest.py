"""Envoi manifeste deployment vers catalogue org."""

from __future__ import annotations

import os
from pathlib import Path
from urllib.request import Request, urlopen


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
    url = os.environ["PROJECT_CATALOG_URL"]
    manifest = Path("config/deployment.env")
    print(publish(manifest_path=manifest, url=url))


if __name__ == "__main__":
    main()
