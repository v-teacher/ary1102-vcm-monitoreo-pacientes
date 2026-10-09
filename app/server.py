"""Servidor HTTP mínimo. Para el entorno cloud, usar TLS en el ingreso."""
import csv
import hmac
import io
import json
import os
import re
from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlsplit
from app.storage import Store


def make_server(address, store, token):
    if len(token) < 16:
        raise ValueError("API_TOKEN debe tener al menos 16 caracteres")

    class Handler(BaseHTTPRequestHandler):
        def log_message(self, format, *args):
            # No registrar rutas, datos o credenciales en el log de acceso.
            print(json.dumps({"component": "http", "request": self.command}), flush=True)

        def respond(self, status, data, content_type="application/json; charset=utf-8"):
            if content_type.startswith("application/json"):
                data = json.dumps(data, ensure_ascii=False)
            body = data.encode("utf-8") if isinstance(data, str) else data
            self.send_response(status)
            self.send_header("Content-Type", content_type)
            self.send_header("Content-Length", str(len(body)))
            self.send_header("Cache-Control", "no-store")
            self.send_header("X-Content-Type-Options", "nosniff")
            self.end_headers()
            self.wfile.write(body)

        def authorized(self):
            supplied = self.headers.get("Authorization", "")
            if hmac.compare_digest(supplied.encode(), ("Bearer " + token).encode()):
                return True
            self.respond(401, {"error": "Token requerido"})
            return False

        def do_GET(self):
            url = urlsplit(self.path)
            if url.path == "/health":
                self.respond(200, {"status": "ok", "mode": "synthetic-only"})
                return
            if url.path == "/":
                self.respond(200, Path(__file__).with_name("dashboard.html").read_bytes(), "text/html; charset=utf-8")
                return
            if not self.authorized():
                return
            if url.path == "/alerts":
                self.respond(200, store.alerts())
                return
            if url.path not in ("/events", "/export.csv"):
                self.respond(404, {"error": "Ruta inexistente"})
                return
            try:
                params = parse_qs(url.query)
                patient = params.get("patient_id", [None])[0]
                if patient and not re.fullmatch(r"SYN-[0-9]{4}", patient):
                    raise ValueError("patient_id inválido")
                def date_param(name):
                    value = params.get(name, [None])[0]
                    if value is None:
                        return None
                    parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
                    if parsed.utcoffset() is None:
                        raise ValueError("Falta zona horaria")
                    return parsed.astimezone(timezone.utc).isoformat()
                since, until = date_param("since"), date_param("until")
                if since and until and since > until:
                    raise ValueError("Ventana temporal invertida")
                limit = int(params.get("limit", ["100"])[0])
                if not 1 <= limit <= 1000:
                    raise ValueError("limit debe estar entre 1 y 1000")
                rows = store.events(patient, since, until, limit)
                if url.path == "/events":
                    self.respond(200, rows)
                else:
                    output = io.StringIO()
                    writer = csv.DictWriter(output, fieldnames=["event_id", "patient_id", "timestamp", "heart_rate", "spo2", "signal_score", "state", "received_at"])
                    writer.writeheader()
                    writer.writerows(rows)
                    self.respond(200, output.getvalue(), "text/csv; charset=utf-8")
            except (ValueError, TypeError) as exc:
                self.respond(400, {"error": str(exc)})

        def do_POST(self):
            if not self.authorized():
                return
            if urlsplit(self.path).path != "/events":
                self.respond(404, {"error": "Ruta inexistente"})
                return
            try:
                size = int(self.headers.get("Content-Length", "0"))
                if not 0 < size <= 4096:
                    raise ValueError("Cuerpo requerido, máximo 4096 bytes")
                result = store.ingest(json.loads(self.rfile.read(size)))
                self.respond(200 if result["duplicate"] else 201, result)
            except FileExistsError as exc:
                self.respond(409, {"error": str(exc)})
            except (ValueError, TypeError, UnicodeError) as exc:
                self.respond(400, {"error": str(exc)})

    return ThreadingHTTPServer(address, Handler)


if __name__ == "__main__":
    store = Store(os.environ.get("DB_PATH", "data/events.sqlite3"))
    server = make_server((os.environ.get("HOST", "127.0.0.1"), int(os.environ.get("PORT", "8080"))), store, os.environ.get("API_TOKEN", ""))
    print("MVP sintético en puerto", server.server_port, flush=True)
    server.serve_forever()
