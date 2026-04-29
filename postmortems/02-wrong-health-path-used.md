# Postmortem 02: Wrong Health Path Returned 404

## Summary

A local check used `/ready`, but this app only exposes `/health` as its health endpoint.

The app was running correctly, but the requested path was wrong.

## Impact

The incorrect check produced a 404 response and could have been mistaken for an application health issue.

No production users or real customers were affected.

## Timeline

- A request was sent to `http://127.0.0.1:8030/ready`.
- The API returned HTTP 404 with the provided request ID.
- A request was sent to `http://127.0.0.1:8030/health`.
- The API returned HTTP 200.
- The server logs showed both paths with their request IDs and status codes.

## Root Cause

The checker used an endpoint name from another context instead of this app's documented `/health` endpoint.

## What Went Well

- The API returned a clear 404 for the unsupported path.
- Request IDs made it possible to connect each response to its structured log line.
- The correct endpoint could be verified quickly with `curl`.

## What Could Improve

- Local support notes should always include the exact endpoint path.
- Before treating a failed check as an app problem, the checker should compare the path with the README.

## Follow-Up Actions

- Keep support scenarios aligned with the actual API surface.
- Use `scripts/check-uptime.sh` for the standard local health check.
- Include both failing and successful request IDs when documenting this scenario.
