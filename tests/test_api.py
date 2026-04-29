import json

from fastapi.testclient import TestClient

from src.main import APP_NAME, REQUEST_ID_HEADER, app


def test_health_returns_ok() -> None:
    client = TestClient(app)

    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {
        "status": "ok",
        "service": APP_NAME,
    }


def test_existing_request_id_is_returned_in_response_header() -> None:
    client = TestClient(app)

    response = client.get("/work", headers={REQUEST_ID_HEADER: "support-case-123"})

    assert response.status_code == 200
    assert response.headers[REQUEST_ID_HEADER] == "support-case-123"
    assert response.json()["request_id"] == "support-case-123"


def test_request_id_is_generated_when_missing() -> None:
    client = TestClient(app)

    response = client.get("/work")

    assert response.status_code == 200
    assert response.headers[REQUEST_ID_HEADER]
    assert response.json()["request_id"] == response.headers[REQUEST_ID_HEADER]


def test_simulated_failure_returns_500_with_request_id() -> None:
    client = TestClient(app)

    response = client.get("/fail", headers={REQUEST_ID_HEADER: "incident-demo-1"})

    assert response.status_code == 500
    assert response.headers[REQUEST_ID_HEADER] == "incident-demo-1"
    assert response.json() == {
        "status": "error",
        "message": "Simulated lab-only failure.",
        "request_id": "incident-demo-1",
    }


def test_request_log_is_structured_json(caplog) -> None:
    client = TestClient(app)

    with caplog.at_level("INFO", logger="uvicorn.error"):
        response = client.get("/health", headers={REQUEST_ID_HEADER: "log-check-1"})

    assert response.status_code == 200

    log_record = next(
        record for record in caplog.records if "request_completed" in record.message
    )
    log_event = json.loads(log_record.message)

    assert log_event["level"] == "info"
    assert log_event["event"] == "request_completed"
    assert log_event["method"] == "GET"
    assert log_event["path"] == "/health"
    assert log_event["status_code"] == 200
    assert log_event["request_id"] == "log-check-1"
    assert isinstance(log_event["duration_ms"], float)
