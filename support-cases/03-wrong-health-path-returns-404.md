# Support Case 03: Wrong Health Path Returns 404

## Scenario

A checker or user calls the wrong health endpoint path.

The app is running, but the requested path is not part of the API.

## Symptom

```bash
curl -s -i -H "X-Request-ID: wrong-path-1" http://127.0.0.1:8030/ready
```

Example result:

```text
HTTP/1.1 404 Not Found
x-request-id: wrong-path-1
```

## Impact

A local checker using the wrong path may report a failure even though the app process is healthy.

For this lab, the impact is confusion during troubleshooting rather than a real customer outage.

## Evidence To Collect

Confirm the reported failing path:

```bash
curl -s -i -H "X-Request-ID: wrong-path-1" http://127.0.0.1:8030/ready
```

Confirm the supported health path:

```bash
curl -s -i -H "X-Request-ID: health-check-1" http://127.0.0.1:8030/health
```

Run the uptime check, which uses `/health`:

```bash
scripts/check-uptime.sh
```

Check the server terminal for structured logs showing the two paths:

```json
{
  "event": "request_completed",
  "path": "/ready",
  "status_code": 404,
  "request_id": "wrong-path-1"
}
```

```json
{
  "event": "request_completed",
  "path": "/health",
  "status_code": 200,
  "request_id": "health-check-1"
}
```

## Findings

The app is reachable, but `/ready` is not a supported endpoint.

The correct local health endpoint is `/health`.

## Likely Cause

The checker or user used an endpoint name from another project or assumed the app had a readiness route.

## Resolution

Update the local check or support instructions to use:

```text
http://127.0.0.1:8030/health
```

## Prevention Or Follow-Up

- Keep README examples aligned with the actual API.
- When a check fails, compare the failing path with the documented endpoints.
- Record both the failing request ID and the successful health-check request ID.
