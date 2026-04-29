# Career Package

## CV-Safe Project Summary

Built a local Observability + Incident Response Lab with FastAPI, structured JSON logs, request ID correlation, a local uptime-check script, support scenarios, a triage runbook, and short postmortems.

## CV-Safe Bullets

- Built a local FastAPI observability lab with health, successful work, and controlled failure endpoints for troubleshooting practice.
- Implemented `X-Request-ID` handling so API responses can be matched with structured JSON request logs.
- Added a simple local uptime-check script and pytest coverage for API behavior, request IDs, logs, and health-check results.
- Documented support-style incident scenarios with symptoms, impact, evidence, likely cause, resolution, and prevention notes.
- Wrote a first-response incident triage runbook and blameless postmortems for local lab incidents.

## Interview Talking Points

### Structured Logs

Structured logs are easier to search and compare because fields such as `path`, `status_code`, and `request_id` are explicit.

In this project, each request log includes the endpoint, status code, duration, and request ID.

### Request IDs

Request IDs connect a user-facing response to the server-side log line for the same request.

In this project, the app accepts an incoming `X-Request-ID` or generates one when missing.

### Uptime Checks

The uptime script checks whether `/health` returns HTTP 200.

It is a local support signal, not production monitoring or alerting.

### Incident Triage

The runbook starts with simple questions:

- Is the app running?
- Does `/health` respond?
- Is the issue endpoint-specific?
- Is there a request ID?
- Is there a matching structured log line?

### Postmortems

The postmortems are short, blameless, and evidence-based.

They focus on impact, timeline, root cause, what went well, what could improve, and follow-up actions.

## What To Avoid Claiming

- Do not claim production incident response experience from this lab.
- Do not claim Kubernetes, distributed tracing, or paid monitoring platform experience from this project.
- Do not describe `/fail` as a real outage. It is a controlled lab-only failure endpoint.
- Do not imply this project handled real customer traffic.
