import json
import logging
import time
from uuid import uuid4

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, Response

APP_NAME = "Observability Incident Response Lab"
REQUEST_ID_HEADER = "X-Request-ID"

logger = logging.getLogger("uvicorn.error")
logger.setLevel(logging.INFO)

app = FastAPI(title=APP_NAME)


def get_request_id(request: Request) -> str:
    existing_request_id = getattr(request.state, "request_id", None)

    if existing_request_id:
        return existing_request_id

    incoming_request_id = request.headers.get(REQUEST_ID_HEADER)

    if incoming_request_id and incoming_request_id.strip():
        return incoming_request_id.strip()

    return str(uuid4())


def write_request_log(
    *,
    method: str,
    path: str,
    status_code: int,
    request_id: str,
    duration_ms: float,
) -> None:
    log_event = {
        "level": "info",
        "event": "request_completed",
        "method": method,
        "path": path,
        "status_code": status_code,
        "request_id": request_id,
        "duration_ms": round(duration_ms, 2),
    }

    logger.info(json.dumps(log_event, sort_keys=True))


@app.middleware("http")
async def add_request_id_and_logging(request: Request, call_next) -> Response:
    request_id = get_request_id(request)
    request.state.request_id = request_id
    start_time = time.perf_counter()

    try:
        response = await call_next(request)
    except Exception:
        duration_ms = (time.perf_counter() - start_time) * 1000
        write_request_log(
            method=request.method,
            path=request.url.path,
            status_code=500,
            request_id=request_id,
            duration_ms=duration_ms,
        )
        raise

    duration_ms = (time.perf_counter() - start_time) * 1000
    response.headers[REQUEST_ID_HEADER] = request_id

    write_request_log(
        method=request.method,
        path=request.url.path,
        status_code=response.status_code,
        request_id=request_id,
        duration_ms=duration_ms,
    )

    return response


@app.get("/health")
def health_check() -> dict[str, str]:
    return {
        "status": "ok",
        "service": APP_NAME,
    }


@app.get("/work")
def simulated_work(request: Request) -> dict[str, str]:
    return {
        "status": "completed",
        "request_id": get_request_id(request),
    }


@app.get("/fail")
def simulated_failure(request: Request) -> JSONResponse:
    return JSONResponse(
        status_code=500,
        content={
            "status": "error",
            "message": "Simulated lab-only failure.",
            "request_id": get_request_id(request),
        },
    )
