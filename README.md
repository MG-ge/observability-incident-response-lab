# Observability + Incident Response Lab

Project 3 in the career lab.

This is a junior-friendly portfolio lab for cloud support, application support, SaaS technical support, product support, and junior operations-adjacent roles.

The project focuses on practical troubleshooting:

- structured logs
- request IDs
- simple uptime checks
- incident scenarios
- runbooks
- postmortem writeups

This is not production experience. It is a local learning and portfolio project.

## Current State

Project 3 v1 is complete.

The project currently has:

- a small FastAPI app
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
- known limitations
- AI usage note
- pytest coverage
- local run script

## Why This Project Exists

Projects 1 and 2 already covered:

- REST API basics
- SQL/data checks
- health and readiness endpoints
- Docker
- GitHub Actions
- CI tests
- deployment-readiness documentation

Project 3 answers a different question:

```text
Can I investigate an application problem using logs, simple signals, runbooks, and incident notes?
```

## Target Roles

- Junior Technical Support Engineer
- SaaS Technical Support Specialist
- Application Support Specialist
- Product Support Engineer
- Cloud Support Engineer, junior or associate level
- API Support Engineer
- Junior Integration Specialist
- Sovellusasiantuntija

## Tech Stack

The stack is intentionally simple:

- Python
- FastAPI
- pytest
- shell scripts
- curl
- local logs

Docker and GitHub Actions may be added later only if they support the observability goal.

## Run Locally

From the project folder:

```bash
cd /Users/mg/Desktop/Dreams/career-lab-2026/observability-incident-response-lab
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest
PORT=8030 scripts/run-dev.sh
```

In another terminal:

```bash
curl -s http://127.0.0.1:8030/health | python -m json.tool
curl -s -H "X-Request-ID: demo-123" http://127.0.0.1:8030/work | python -m json.tool
curl -s -i -H "X-Request-ID: incident-demo-1" http://127.0.0.1:8030/fail
```

Watch the server terminal for structured request logs.

Run the local uptime check:

```bash
scripts/check-uptime.sh
```

Expected healthy result:

```text
uptime_check=pass
url=http://127.0.0.1:8030/health
http_status=200
request_id=uptime-check-local
next_action=No action needed.
```

## Run Tests

```bash
pytest
```

Expected result:

```text
7 passed
```

## v1 Scope

Project 3 v1 includes:

- a small local API
- structured logs
- request ID behavior
- one simple uptime-check workflow
- support-style incident scenarios
- a runbook
- short postmortems
- known limitations
- AI usage note

## Incident Scenarios

The support scenarios are in `support-cases/`:

- `01-uptime-check-app-not-running.md`
- `02-lab-failure-endpoint-returns-500.md`
- `03-wrong-health-path-returns-404.md`

## Runbook And Postmortems

The first-response runbook is in `runbooks/`:

- `incident-triage.md`

The lab postmortems are in `postmortems/`:

- `01-uptime-check-app-not-running.md`
- `02-wrong-health-path-used.md`

## Final Review And Career Package

Final documentation is in `docs/`:

- `project-review.md`
- `career-package.md`
- `known-limitations.md`
- `ai-usage.md`

## Not In Scope

- Kubernetes
- microservices
- frontend work
- complex authentication
- paid monitoring tools
- real production deployment
- production incident claims
- senior SRE/platform engineering claims

## Start Here

Read the plan:

```bash
cat docs/project-plan.md
cat STATUS.md
cat NEXT_STEPS.md
```
