# Project Review

## Status

Project 3 v1 is complete as a local portfolio lab.

It demonstrates junior-ready observability and incident-response basics without claiming production monitoring experience.

## What Was Built

- Small FastAPI app with `GET /health`, `GET /work`, and `GET /fail`.
- Request ID handling with `X-Request-ID`.
- Structured JSON request logs.
- Local uptime-check script for `/health`.
- Pytest coverage for API behavior, request IDs, logs, and the uptime script.
- Three support-style incident scenarios.
- One incident triage runbook.
- Two short blameless lab postmortems.

## What This Proves

- Can connect an API response to a structured log using a request ID.
- Can distinguish app availability from endpoint-specific behavior.
- Can use a simple uptime check as a support signal.
- Can document symptoms, impact, evidence, findings, likely cause, resolution, and prevention.
- Can write a practical first-response runbook.
- Can write short blameless postmortems from evidence.

## What This Does Not Prove

- Production on-call experience.
- Distributed tracing.
- Kubernetes or platform engineering experience.
- Paid observability platform administration.
- Incident management for real customers.

## Validation

Run from the project folder:

```bash
pytest
```

Expected result:

```text
7 passed
```

Manual local check:

```bash
PORT=8030 scripts/run-dev.sh
```

In another terminal:

```bash
scripts/check-uptime.sh
```

Expected result:

```text
uptime_check=pass
http_status=200
```

## Reviewer Path

Start with:

- `README.md`
- `src/main.py`
- `tests/test_api.py`
- `tests/test_uptime_script.py`
- `scripts/check-uptime.sh`
- `support-cases/`
- `runbooks/incident-triage.md`
- `postmortems/`
- `docs/known-limitations.md`
