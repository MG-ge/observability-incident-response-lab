#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

HOST="${HOST:-127.0.0.1}"
PORT="${PORT:-8030}"
BASE_URL="${BASE_URL:-http://$HOST:$PORT}"
REQUEST_ID="${REQUEST_ID:-uptime-check-local}"
HEALTH_URL="${BASE_URL%/}/health"

if ! command -v curl >/dev/null 2>&1; then
  echo "uptime_check=fail"
  echo "reason=curl_not_found"
  echo "next_action=Install curl or run this check from an environment that has curl."
  exit 1
fi

set +e
HTTP_STATUS="$(
  curl \
    --silent \
    --show-error \
    --output /dev/null \
    --write-out "%{http_code}" \
    --header "X-Request-ID: $REQUEST_ID" \
    "$HEALTH_URL"
)"
CURL_EXIT_CODE=$?
set -e

if [ "$CURL_EXIT_CODE" -ne 0 ]; then
  echo "uptime_check=fail"
  echo "url=$HEALTH_URL"
  echo "http_status=unavailable"
  echo "request_id=$REQUEST_ID"
  echo "next_action=Confirm the app is running with PORT=$PORT scripts/run-dev.sh, then retry."
  exit 1
fi

if [ "$HTTP_STATUS" = "200" ]; then
  echo "uptime_check=pass"
  echo "url=$HEALTH_URL"
  echo "http_status=$HTTP_STATUS"
  echo "request_id=$REQUEST_ID"
  echo "next_action=No action needed."
  exit 0
fi

echo "uptime_check=fail"
echo "url=$HEALTH_URL"
echo "http_status=$HTTP_STATUS"
echo "request_id=$REQUEST_ID"
echo "next_action=Check the API logs for this request ID and confirm /health is healthy."
exit 1
