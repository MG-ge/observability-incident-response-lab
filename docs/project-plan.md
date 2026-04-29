# Project Plan

## Project Name

Observability + Incident Response Lab

## Portfolio Purpose

This is Project 3 in the career lab.

It builds on:

- Project 1: `b2b-saas-support-lab`
- Project 2: `cloud-api-cicd-lab`

Project 1 proved SaaS/application support basics:

- REST API usage
- SQLite/data checks
- HTTP status-code reasoning
- support cases
- runbooks
- tests

Project 2 proved cloud/application support basics:

- environment variables
- health and readiness checks
- Docker build/run basics
- GitHub Actions CI
- secrets-handling notes
- rollback/redeploy notes

Project 3 should prove:

- log reading
- structured logging
- request correlation with request IDs
- basic metrics or uptime-check thinking
- incident triage
- runbook usage
- post-incident communication

The project should be easy to explain:

```text
I built a small local API with observable behavior, used structured logs and simple checks to investigate failures, and documented incidents with runbooks and postmortems.
```

This must be described as a portfolio lab, not production experience.

## Target Roles

Good target roles:

- Junior Technical Support Engineer
- SaaS Technical Support Specialist
- Application Support Specialist
- Product Support Engineer
- Cloud Support Engineer, junior or associate level
- API Support Engineer
- Junior Integration Specialist
- Sovellusasiantuntija
- Junior Operations or SRE-adjacent roles

## Success Criteria For v1

Version 1 is successful when a reviewer can see:

- a small API that runs locally
- a health endpoint
- structured log output
- request IDs in logs or responses
- pytest coverage for core behavior
- one simple metrics or uptime-check workflow
- support cases based on observable symptoms
- an incident triage runbook
- at least two short postmortems
- known limitations
- honest AI usage note

## Technical Stack

Use a simple backend stack:

- Python
- FastAPI
- pytest
- shell scripts
- curl
- local log output

Do not add a database unless there is a clear support reason. Project 1 already covered SQL/data investigation.

Do not add Docker or GitHub Actions at the start. Project 2 already proved those basics. They may be reused later only if they support the observability story.

## Planned API Surface

Keep the API small.

Likely endpoints:

### `GET /health`

Purpose:

```text
Shows that the API process is alive.
```

### `GET /work`

Purpose:

```text
Creates a normal successful request that can be seen in logs and metrics.
```

### `GET /fail`

Purpose:

```text
Creates a controlled application error for local incident practice.
```

This endpoint should be clearly documented as a lab-only simulation endpoint.

### Optional `GET /metrics`

Purpose:

```text
Shows simple local counters such as request count and error count.
```

If `/metrics` makes the app too complicated, use a local uptime-check script instead.

## Structured Logging Plan

Logs should be readable by a junior support person.

Each important request log should include:

- timestamp
- level
- event name
- method
- path
- status code
- request ID

Example shape:

```json
{
  "level": "info",
  "event": "request_completed",
  "method": "GET",
  "path": "/health",
  "status_code": 200,
  "request_id": "example-request-id"
}
```

Do not log secrets, tokens, passwords, or full environment dumps.

## Request ID Plan

Request IDs help connect:

- one user report
- one API response
- one log line
- one incident note

The app should either:

- accept an incoming `X-Request-ID` header
- or generate a simple request ID when one is missing

The request ID should be visible in the response headers or response body and in logs.

## Metrics Or Uptime Check Plan

Choose one simple v1 option.

Option A:

```text
Add a basic /metrics endpoint with local in-memory counters.
```

Option B:

```text
Add a script that checks /health and writes a small uptime-check result.
```

Option B may be better if metrics would distract from the support workflow.

Chosen v1 approach: Option B, a local uptime-check script.

## Incident Scenario Plan

Add at least three support-style incident scenarios.

Suggested scenarios:

- API is alive but a lab-only failure endpoint returns 500.
- Several failed requests appear with the same request ID pattern.
- Uptime check fails because the app is not running.

Implemented Slice 3 scenarios:

- Uptime check fails because the app is not running.
- Lab-only failure endpoint returns 500 with a matching request ID.
- Wrong health path returns 404 while `/health` succeeds.

Each scenario should include:

- symptom
- customer or user impact
- evidence
- commands used
- findings
- likely cause
- resolution
- prevention or follow-up

## Runbook Plan

Create a runbook for first-response triage.

It should answer:

- Is the app running?
- Is `/health` responding?
- Are errors visible in logs?
- Is there a request ID?
- Is the problem repeatable?
- What should be documented before escalation?

Implemented Slice 4 runbook:

- `runbooks/incident-triage.md`

## Postmortem Plan

Create at least two short postmortems.

Each should include:

- summary
- impact
- timeline
- root cause
- what went well
- what could improve
- follow-up actions

Keep the tone blameless and practical.

Implemented Slice 4 postmortems:

- `postmortems/01-uptime-check-app-not-running.md`
- `postmortems/02-wrong-health-path-used.md`

## Final Review And Career Package

Implemented Slice 5 documents:

- `docs/project-review.md`
- `docs/career-package.md`
- `docs/known-limitations.md`
- `docs/ai-usage.md`

## Explicit Exclusions

Do not add:

- Kubernetes
- microservices
- frontend
- database
- complex auth
- distributed tracing
- paid observability services
- production alerting
- real production secrets
- fake production incident claims

## Suggested Implementation Slices

### Slice 0: Plan Review

Review this document before writing code.

### Slice 1: Local API And Logs

Implement:

- basic FastAPI app
- `/health`
- structured logs
- request ID behavior
- tests

### Slice 2: Basic Signal

Implement one:

- basic `/metrics`
- or uptime-check script

### Slice 3: Incident Documentation

Add support cases for observable failures.

### Slice 4: Runbook And Postmortems

Add runbook and postmortems.

### Slice 5: Final Review And Career Package

Add final review, career package, and interview practice notes.

## What I Must Understand Manually

Before implementation, be able to explain:

- what a structured log is
- why request IDs matter
- what an uptime check proves
- what a metric proves
- what a runbook is
- what a postmortem is
- why this is not production incident response experience
