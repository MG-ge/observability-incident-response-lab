# Incident Triage Runbook

## Purpose

Use this runbook when the local lab API appears unhealthy, returns errors, or has confusing request behavior.

This runbook is for a portfolio lab. It is not a production on-call process.

## First Response Checklist

### 1. Confirm The App Is Expected To Be Running

From the project folder:

```bash
pwd
```

Expected folder:

```text
/Users/mg/Desktop/Dreams/career-lab-2026/observability-incident-response-lab
```

Start the app if it is not already running:

```bash
PORT=8030 scripts/run-dev.sh
```

Keep this terminal open so request logs are visible.

### 2. Check Basic Uptime

In another terminal:

```bash
scripts/check-uptime.sh
```

Healthy result:

```text
uptime_check=pass
http_status=200
```

If the result is `uptime_check=fail`, record:

- `url`
- `http_status`
- `request_id`
- `next_action`

### 3. Check `/health` Directly

```bash
curl -s -i -H "X-Request-ID: triage-health-1" http://127.0.0.1:8030/health
```

Expected result:

```text
HTTP/1.1 200 OK
x-request-id: triage-health-1
```

If `/health` fails, document the status code and response body before changing anything.

### 4. Check Whether Normal Work Still Succeeds

```bash
curl -s -i -H "X-Request-ID: triage-work-1" http://127.0.0.1:8030/work
```

Expected result:

```text
HTTP/1.1 200 OK
x-request-id: triage-work-1
```

If `/health` succeeds but `/work` fails, the app is reachable but the behavior is endpoint-specific.

### 5. Reproduce A Known Lab Error

Only use `/fail` when you intentionally want the simulated failure:

```bash
curl -s -i -H "X-Request-ID: triage-fail-1" http://127.0.0.1:8030/fail
```

Expected result:

```text
HTTP/1.1 500 Internal Server Error
x-request-id: triage-fail-1
```

This confirms the lab-only failure path and request ID behavior.

### 6. Match The Request ID To Logs

Look at the server terminal for a structured log line with the same request ID.

Example:

```json
{
  "event": "request_completed",
  "path": "/fail",
  "status_code": 500,
  "request_id": "triage-fail-1"
}
```

The request ID connects the user-facing response to the server-side log event.

### 7. Decide The Likely Category

Use the evidence to choose the closest category:

- App not running: uptime check cannot reach `/health`.
- Wrong path: one path returns 404 while `/health` returns 200.
- Simulated lab failure: `/fail` returns 500 by design.
- Unknown issue: behavior does not match the documented scenarios.

### 8. Document Before Escalating

Capture:

- symptom
- impact
- command used
- response status code
- response body when relevant
- request ID
- matching log line
- likely cause
- next action

## Escalation Notes

Escalate or investigate further if:

- `/health` fails after the app is confirmed running
- request IDs are missing from responses or logs
- a non-`/fail` endpoint returns 500
- behavior is repeatable but not covered by an existing support case

Do not claim a production outage. This project is a local lab.
