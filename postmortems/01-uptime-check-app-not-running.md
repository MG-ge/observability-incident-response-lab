# Postmortem 01: Uptime Check Failed Because App Was Not Running

## Summary

The local uptime check failed because the FastAPI app was not running on the expected port.

This was a lab incident used to practice basic first-response triage.

## Impact

The `/health` endpoint could not be reached locally.

No production users or real customers were affected.

## Timeline

- The uptime check was run with `scripts/check-uptime.sh`.
- The check returned `uptime_check=fail` and `http_status=unavailable`.
- The app process was started with `PORT=8030 scripts/run-dev.sh`.
- The uptime check was rerun.
- The check returned `uptime_check=pass` and `http_status=200`.

## Root Cause

The API process was not running when the uptime check was executed.

## What Went Well

- The uptime check gave a clear failure signal.
- The output included the checked URL and a request ID.
- The `next_action` message pointed to the correct recovery step.

## What Could Improve

- The operator should confirm the app terminal is running before starting a scenario.
- The README should remain clear about using two terminals for local checks.

## Follow-Up Actions

- Keep the local run command visible in the README.
- Use the incident triage runbook before writing a support case.
- Record the uptime-check output in future incident notes.
