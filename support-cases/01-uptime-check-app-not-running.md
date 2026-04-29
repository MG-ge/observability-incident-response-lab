# Support Case 01: Uptime Check Fails When App Is Not Running

## Scenario

The local uptime check reports that `/health` is unavailable.

This is a lab scenario for practicing first-response support triage. It is not production monitoring.

## Symptom

```bash
scripts/check-uptime.sh
```

Example result:

```text
uptime_check=fail
url=http://127.0.0.1:8030/health
http_status=unavailable
request_id=uptime-check-local
next_action=Confirm the app is running with PORT=8030 scripts/run-dev.sh, then retry.
```

## Impact

A user or support engineer cannot confirm that the API process is responding locally.

For this lab, the impact is limited to local testing and incident-response practice.

## Evidence To Collect

Check the uptime signal:

```bash
scripts/check-uptime.sh
```

Check whether the app responds directly:

```bash
curl -s -i http://127.0.0.1:8030/health
```

Start the app if needed:

```bash
PORT=8030 scripts/run-dev.sh
```

Retry from another terminal:

```bash
scripts/check-uptime.sh
```

## Findings

If the app is not running, the uptime check cannot connect to `/health`.

After the app starts, the expected result is:

```text
uptime_check=pass
http_status=200
```

## Likely Cause

The FastAPI app was not started, or it was stopped before the uptime check ran.

## Resolution

Start the app on the expected local port:

```bash
PORT=8030 scripts/run-dev.sh
```

Then rerun:

```bash
scripts/check-uptime.sh
```

## Prevention Or Follow-Up

- Keep the app terminal visible while practicing incident scenarios.
- Record the uptime-check output in the incident note.
- Confirm the port before assuming the app itself is broken.
