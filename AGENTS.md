# AGENTS.md

## Project Purpose

Observability + Incident Response Lab is Project 3 in the career lab.

It builds on:

- Project 1: B2B SaaS Support Lab
- Project 2: Cloud API + CI/CD Lab

Project 3 should prove junior-ready troubleshooting around:

- structured logs
- request IDs
- basic metrics or uptime checks
- incident scenarios
- runbooks
- postmortem writeups

This is a portfolio lab, not production experience.

## Target Roles

This project should support applications for:

- Junior Technical Support Engineer
- SaaS Technical Support Specialist
- Application Support Specialist
- Product Support Engineer
- Cloud Support Engineer, junior or associate level
- API Support Engineer
- Junior Integration Specialist
- Junior Operations or SRE-adjacent roles
- Sovellusasiantuntija

## Build Direction

Keep the project small, local, and support-focused.

Prefer:

- one small FastAPI service
- local development first
- clear health and readiness behavior
- structured application logs
- a simple request ID pattern
- a basic metrics or uptime-check workflow
- documented incident scenarios
- practical runbooks
- short postmortems
- pytest tests for important behavior

Avoid:

- Kubernetes
- microservices
- frontend work
- complex authentication
- paid monitoring services
- real production secrets
- fake production claims
- broad platform engineering claims

## Engineering Rules

- Do not start implementation until the project plan is reviewed.
- Make small, reversible changes.
- Add tests for new behavior once implementation starts.
- Keep commands copy-pasteable.
- Prefer boring, explicit, readable code.
- Document support evidence: command, result, interpretation, next action.
- Do not commit real secrets.

## Portfolio Rule

This project should show that the owner can:

- read logs and connect them to API behavior
- understand why request IDs help support investigations
- explain basic metrics or uptime checks
- identify symptoms, impact, likely cause, and resolution
- write a runbook a junior support engineer could follow
- write a clear postmortem without blaming people
- explain what this lab proves and what it does not prove
