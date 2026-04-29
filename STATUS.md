# STATUS.md

## Current Phase

Project 3 v1 complete.

## Current State

Project 3 has a small local FastAPI app, a simple uptime-check workflow, support-style incident scenarios, an incident triage runbook, short lab postmortems, and final career-positioning documentation.

Created:

- project planning scaffold
- initial README
- initial next steps
- project plan
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

Optional future additions:

- Dockerfile
- GitHub Actions workflow

## Project 3 Goal

Project 3 should prove junior-ready observability and incident response thinking for cloud/application support roles.

The project should stay small and local.

## Current Decision

Next step:

```text
Project 3 v1 is complete. Optional future improvements should stay small and support the observability story.
```

## Completion Criteria For v1

Project 3 v1 should be considered complete only when:

- the app runs locally
- tests pass
- structured logs are implemented and documented
- request IDs are visible in logs or responses
- a basic metrics or uptime-check workflow exists
- at least three incident scenarios exist
- at least one runbook exists
- at least two postmortems exist
- known limitations are documented
- AI usage is documented honestly

## Not In Scope For v1

- Kubernetes
- distributed tracing
- production monitoring
- paid observability platforms
- real cloud deployment
- complex authentication
- database
- frontend UI
- incident automation
- on-call tooling
- senior SRE claims
