# Support Case 02: Lab Failure Endpoint Returns 500

## Scenario

A request to `/fail` returns a controlled HTTP 500 response.

This endpoint exists only to create a repeatable lab incident signal.

## Symptom

```bash
curl -s -i -H "X-Request-ID: incident-demo-1" http://127.0.0.1:8030/fail
```

Example response:

```text
HTTP/1.1 500 Internal Server Error
x-request-id: incident-demo-1
```

Response body:

```json
{
  "status": "error",
  "message": "Simulated lab-only failure.",
  "request_id": "incident-demo-1"
}
```

## Impact

The request fails for the caller.

For this lab, the impact is intentional and limited to local incident practice.

## Evidence To Collect

Send a request with a known request ID:

```bash
curl -s -i -H "X-Request-ID: incident-demo-1" http://127.0.0.1:8030/fail
```

Confirm the app is otherwise alive:

```bash
curl -s http://127.0.0.1:8030/health | python -m json.tool
```

Check the server terminal for a structured log line like:

```json
{
  "event": "request_completed",
  "path": "/fail",
  "status_code": 500,
  "request_id": "incident-demo-1"
}
```

## Findings

The response header, response body, and structured log all include the same request ID.

This lets support connect the failed API response to the matching log event.

## Likely Cause

The `/fail` endpoint was called. It is designed to return a lab-only simulated error.

## Resolution

No code fix is required for this scenario.

Use `/work` for a successful lab request:

```bash
curl -s -H "X-Request-ID: work-check-1" http://127.0.0.1:8030/work | python -m json.tool
```

## Prevention Or Follow-Up

- Document that `/fail` is a simulation endpoint.
- Include the request ID in any incident note.
- Do not describe this as a production outage.
