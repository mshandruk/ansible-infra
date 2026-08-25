from dataclasses import dataclass
import subprocess
import socket
import http.server
import socketserver
import argparse


@dataclass(frozen=True, slots=True)
class HostInfo:
    uptime: str
    hostname: str


def get_host_info() -> HostInfo:
    try:
        result = subprocess.run(
            ["uptime", "-p"],
            capture_output=True,
            text=True,
            check=True,
            timeout=5,
        )
        uptime = result.stdout.strip()
    except (subprocess.SubprocessError, FileNotFoundError):
        uptime = "Unknown"

    hostname = socket.gethostname()
    return HostInfo(uptime, hostname)


class MonitoringHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            host_info = get_host_info()
            html = f"""
            <!DOCTYPE html>
            <html lang="ru">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Мониторинг</title>
                <style>
                    body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; background: #f4f7f6; color: #333; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }}
                    .card {{ background: white; padding: 30px; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.05); width: 100%; max-width: 400px; }}
                    h1 {{ font-size: 20px; margin-top: 0; color: #111; border-bottom: 2px solid #f0f0f0; padding-bottom: 15px; }}
                    .info-row {{ display: flex; justify-content: space-between; margin: 15px 0; font-size: 15px; }}
                    .label {{ font-weight: 600; color: #666; }}
                    .value {{ color: #0076ff; font-family: monospace; font-size: 16px; }}
                </style>
            </head>
            <body>
            
                <div class="card">
                    <h1>Статус хоста</h1>
                    <div class="info-row">
                        <span class="label">Имя хоста (Hostname):</span>
                        <span class="value">{host_info.hostname}</span>
                    </div>
                    <div class="info-row">
                        <span class="label">Время работы (Uptime):</span>
                        <span class="value">{host_info.uptime}</span>
                    </div>
                </div>
            
            </body>
            </html>
            """

            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(html.encode("utf-8"))
        else:
            self.send_error(404, "Page Not Found")


@dataclass(frozen=True, slots=True)
class AppConfig:
    address: str
    port: int


def parse_args() -> AppConfig:
    parser = argparse.ArgumentParser(description="Host monitor Web App")

    default_address = "127.0.0.1"
    parser.add_argument(
        "--address",
        type=str,
        default=default_address,
        help=f"Listen address (default: {default_address})",
    )

    default_port = 8000
    parser.add_argument(
        "--port",
        type=int,
        default=default_port,
        help=f"Listen port (default: {default_port})",
    )
    args = parser.parse_args()

    return AppConfig(args.address, args.port)


if __name__ == "__main__":
    config = parse_args()

    server = socketserver.TCPServer(
        (config.address, config.port),
        MonitoringHandler,  # type: ignore
        bind_and_activate=False,
    )
    server.allow_reuse_address = True
    try:
        server.server_bind()
        server.server_activate()
        with server:
            print(f"Server is running: {config.address}:{config.port}")
            server.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped")
