# NEXT_STEPS.md

## Current Recommendation

Project 3 v1 is complete.

Project 3 should be:

```text
Observability + Incident Response Lab
```

## Why This Project Comes Next

Project 1 proved SaaS support basics:

- APIs
- SQLite/data checks
- tickets
- support cases
- runbooks

Project 2 proved cloud/application support basics:

- environment variables
- health and readiness
- Docker
- GitHub Actions
- CI tests
- secrets-handling notes
- rollback/redeploy notes

Project 3 should prove the next support skill:

```text
Can I investigate what happened when an application is unhealthy, noisy, slow, or failing?
```

## Current State

Project 3 v1 is implemented:

- local FastAPI app
- `GET /health`
- `GET /work`
- `GET /fail`
- structured request logs
- request ID handling with `X-Request-ID`
- local uptime-check script
- support-style incident scenarios
- incident triage runbook
- short lab postmortems
- final project review
- career package
- known limitations document
- AI usage note
- pytest coverage
- local run script

## Final Review Checklist

Confirm you can explain:

- what a structured log is
- why request IDs help support investigations
- how `/fail` creates a lab-only incident signal
- why this is not production monitoring
- how the local uptime-check script differs from production monitoring
- how to document symptom, impact, evidence, likely cause, resolution, and prevention
- how the runbook guides first-response triage
- why postmortems should be blameless and evidence-based
- what this lab proves and what it does not prove

## Planned Slices

### Slice 1: Local App And Structured Logs

Add a small API with:

- `/health`
- structured JSON-style logs
- request ID handling
- tests for basic behavior

Status: complete.

### Slice 2: Basic Metrics Or Uptime Checks

Add one simple observability signal:

- either a basic `/metrics` endpoint
- or a local uptime-check script

Keep it beginner-readable.

Recommended choice: uptime-check script first.

Reason:

```text
It proves application support troubleshooting without adding more API state or complexity.
```

Status: complete.

### Slice 3: Incident Scenarios

Document realistic support scenarios:

- service healthy but readiness/config problem
- repeated application error
- slow response or degraded behavior

Each scenario should include:

- symptom
- impact
- evidence
- investigation steps
- likely cause
- resolution
- prevention

Status: complete.

### Slice 4: Runbook And Postmortems

Add:

- one incident triage runbook
- at least two short postmortems

Status: complete.

### Slice 5: Final Review And Career Package

Add:

- project review
- CV-safe bullets
- interview talking points
- honest AI usage note

Status: complete.

## Optional Future Improvements

Only add these if they support the observability story:

- simple `/metrics` endpoint
- GitHub Actions test workflow
- Dockerfile for repeatable local runs
- additional support scenarios

## Do Not Add Yet

- Kubernetes
- frontend
- authentication
- database
- paid monitoring service
- production alerting platform
- real cloud deployment
- complex distributed tracing

## What To Understand Before Coding

- What a structured log is.
- Why request IDs help connect one user request to logs.
- What a metric is.
- How uptime checks differ from unit tests.
- What an incident runbook is.
- What a postmortem is and why it should be blameless.
