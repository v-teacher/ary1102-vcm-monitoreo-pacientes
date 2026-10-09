"""Persistencia de una réplica para laboratorio local, no compartida entre tareas."""
import json
import sqlite3
from datetime import datetime, timezone
from pathlib import Path
from app.domain import classify, validate_event


class Store:
    def __init__(self, path):
        self.path = str(path)
        Path(path).parent.mkdir(parents=True, exist_ok=True)
        with self.connect() as conn:
            conn.execute("PRAGMA journal_mode=WAL")
            conn.execute("CREATE TABLE IF NOT EXISTS events (event_id TEXT PRIMARY KEY, patient_id TEXT NOT NULL, timestamp TEXT NOT NULL, state TEXT NOT NULL, payload TEXT NOT NULL, received_at TEXT NOT NULL)")
            conn.execute("CREATE INDEX IF NOT EXISTS patient_time ON events(patient_id, timestamp)")
            conn.execute("CREATE TABLE IF NOT EXISTS alerts (event_id TEXT PRIMARY KEY REFERENCES events(event_id), status TEXT NOT NULL, created_at TEXT NOT NULL)")

    def connect(self):
        conn = sqlite3.connect(self.path, timeout=10)
        conn.row_factory = sqlite3.Row
        conn.execute("PRAGMA foreign_keys=ON")
        return conn

    def ingest(self, raw):
        event = validate_event(raw)
        payload = json.dumps(event, sort_keys=True, ensure_ascii=False)
        with self.connect() as conn:
            conn.execute("BEGIN IMMEDIATE")
            previous = conn.execute("SELECT payload, state FROM events WHERE event_id=?", (event["event_id"],)).fetchone()
            if previous:
                if previous["payload"] != payload:
                    raise FileExistsError("event_id existente con contenido diferente")
                return {"event_id": event["event_id"], "state": previous["state"], "duplicate": True}
            state = classify(event)
            now = datetime.now(timezone.utc).isoformat()
            conn.execute("INSERT INTO events VALUES (?,?,?,?,?,?)", (event["event_id"], event["patient_id"], event["timestamp"], state, payload, now))
            if state == "Crítico":
                conn.execute("INSERT INTO alerts VALUES (?, 'PENDIENTE', ?)", (event["event_id"], now))
        return {"event_id": event["event_id"], "state": state, "duplicate": False}

    def events(self, patient=None, since=None, until=None, limit=100):
        query, parameters = "SELECT * FROM events WHERE 1=1", []
        for column, op, value in [("patient_id", "=", patient), ("timestamp", ">=", since), ("timestamp", "<=", until)]:
            if value is not None:
                query += f" AND {column} {op} ?"
                parameters.append(value)
        query += " ORDER BY timestamp DESC, event_id LIMIT ?"
        parameters.append(limit)
        with self.connect() as conn:
            rows = conn.execute(query, parameters).fetchall()
        return [{**json.loads(r["payload"]), "state": r["state"], "received_at": r["received_at"]} for r in rows]

    def alerts(self):
        with self.connect() as conn:
            return [dict(r) for r in conn.execute("SELECT alerts.*, events.patient_id, events.state FROM alerts JOIN events USING(event_id) ORDER BY created_at DESC LIMIT 100")]
