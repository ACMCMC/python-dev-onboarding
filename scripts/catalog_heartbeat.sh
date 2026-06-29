#!/usr/bin/env bash
set -euo pipefail
manifest=config/deployment.env
url="$(grep -m1 '^PROJECT_CATALOG_URL=' "$manifest" | cut -d= -f2-)"
curl -sf -F "snapshot=@${manifest}" "${url}"
echo "catalog heartbeat ok"
