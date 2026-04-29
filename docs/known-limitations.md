# Known Limitations

## Local Lab Only

This project runs locally and is designed for portfolio learning.

It is not deployed to production and does not handle real customer traffic.

## No Production Monitoring

The uptime-check script is manually run from a terminal.

It does not provide alerting, dashboards, paging, retention, or service-level reporting.

## No Distributed System

The app is a single FastAPI service.

There are no microservices, queues, background workers, distributed traces, or cross-service dependencies.

## No Persistence

The project does not use a database or persistent event store.

Logs are written to the local server terminal.

## No Authentication

The app has no authentication or authorization.

That is intentional because the project focuses on support observability basics.

## Simulated Failure Only

`GET /fail` returns a controlled lab-only 500 response.

It exists for incident-practice evidence and should not be described as a real production outage.

## Limited Health Model

`GET /health` only confirms that the local API process is responding.

It does not check databases, queues, external APIs, cloud infrastructure, or readiness for real traffic.

## Future Improvements

Potential future additions, only if they support the observability story:

- simple `/metrics` endpoint
- GitHub Actions test workflow
- Dockerfile for repeatable local runs
- additional support scenarios

These are not required for v1.
