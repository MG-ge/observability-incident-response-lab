import os
import subprocess
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = PROJECT_ROOT / "scripts" / "check-uptime.sh"


class HealthHandler(BaseHTTPRequestHandler):
    response_status = 200

    def do_GET(self) -> None:
        if self.path != "/health":
            self.send_response(404)
            self.end_headers()
            return

        self.send_response(self.response_status)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(b'{"status":"ok"}')

    def log_message(self, format: str, *args) -> None:
        return


def run_test_server(status_code: int) -> tuple[HTTPServer, str]:
    handler = type(
        f"HealthHandler{status_code}",
        (HealthHandler,),
        {"response_status": status_code},
    )
    server = HTTPServer(("127.0.0.1", 0), handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    host, port = server.server_address
    return server, f"http://{host}:{port}"


def run_uptime_check(base_url: str) -> subprocess.CompletedProcess[str]:
    env = {
        **os.environ,
        "BASE_URL": base_url,
        "REQUEST_ID": "uptime-test-1",
    }

    return subprocess.run(
        ["bash", str(SCRIPT_PATH)],
        cwd=PROJECT_ROOT,
        env=env,
        text=True,
        capture_output=True,
        check=False,
    )


def test_uptime_script_passes_when_health_returns_200() -> None:
    server, base_url = run_test_server(200)

    try:
        result = run_uptime_check(base_url)
    finally:
        server.shutdown()

    assert result.returncode == 0
    assert "uptime_check=pass" in result.stdout
    assert f"url={base_url}/health" in result.stdout
    assert "http_status=200" in result.stdout
    assert "request_id=uptime-test-1" in result.stdout


def test_uptime_script_fails_when_health_is_not_200() -> None:
    server, base_url = run_test_server(500)

    try:
        result = run_uptime_check(base_url)
    finally:
        server.shutdown()

    assert result.returncode == 1
    assert "uptime_check=fail" in result.stdout
    assert f"url={base_url}/health" in result.stdout
    assert "http_status=500" in result.stdout
    assert "request_id=uptime-test-1" in result.stdout
