#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

if [ -x ".venv/bin/python" ]; then
  PYTHON=".venv/bin/python"
else
  PYTHON="${PYTHON:-python3}"
fi

HOST="${HOST:-127.0.0.1}"
PORT="${PORT:-8030}"

exec "$PYTHON" -m uvicorn src.main:app --reload --host "$HOST" --port "$PORT"
