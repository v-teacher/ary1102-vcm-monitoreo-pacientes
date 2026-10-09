import json
import tempfile
import threading
import unittest
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.error import HTTPError
from app.domain import classify, validate_event
from app.storage import Store
from app.server import make_server

TOKEN = "synthetic-test-token-1234"


def event(score=90):
    return dict(event_id="test-1", patient_id="SYN-0001", timestamp="2026-10-09T12:00:00Z", heart_rate=80, spo2=98, signal_score=score)


class AppTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.store = Store(Path(self.tmp.name) / "events.sqlite3")

    def tearDown(self):
        self.tmp.cleanup()

    def test_classification_boundaries(self):
        for score, expected in [(0,"Normal"),(39,"Normal"),(40,"Precaución"),(69,"Precaución"),(70,"Crítico"),(100,"Crítico")]:
            self.assertEqual(classify(validate_event(event(score))), expected)

    def test_invalid_and_personal_fields(self):
        for changes in [{"name":"Persona"},{"patient_id":"real-person"},{"signal_score":float("nan")},{"spo2":True},{"timestamp":"2026-10-09"}]:
            with self.assertRaises(ValueError):
                validate_event({**event(), **changes})

    def test_idempotency_conflict_and_persistence(self):
        self.assertFalse(self.store.ingest(event())["duplicate"])
        self.assertTrue(self.store.ingest(event())["duplicate"])
        self.assertEqual(len(self.store.alerts()), 1)
        with self.assertRaises(FileExistsError):
            self.store.ingest(event(10))
        reopened = Store(self.store.path)
        self.assertEqual(len(reopened.events("SYN-0001")), 1)
        self.assertEqual(reopened.events("SYN-0002"), [])
        self.assertEqual(reopened.events(since="2026-10-10T00:00:00+00:00"), [])

    def test_simultaneous_duplicates_create_single_alert(self):
        with ThreadPoolExecutor(max_workers=8) as executor:
            results = list(executor.map(lambda _: self.store.ingest(event()), range(20)))
        self.assertEqual(sum(not r["duplicate"] for r in results), 1)
        self.assertEqual(len(self.store.events()), 1)
        self.assertEqual(len(self.store.alerts()), 1)

    def test_fixture_states(self):
        fixture = Path(__file__).resolve().parents[1] / "datasets/telemetria-sintetica.jsonl"
        states = [self.store.ingest(json.loads(line))["state"] for line in fixture.read_text().splitlines()]
        self.assertEqual(states, ["Normal", "Precaución", "Crítico"])

    def test_http_flow_auth_window_and_export(self):
        server = make_server(("127.0.0.1", 0), self.store, TOKEN)
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        base = f"http://127.0.0.1:{server.server_port}"
        def call(path, data=None, token=TOKEN):
            request = Request(base+path, data=json.dumps(data).encode() if data is not None else None, headers={"Authorization":"Bearer "+token,"Content-Type":"application/json"})
            return urlopen(request, timeout=5)
        try:
            with call("/health", token="") as response:
                self.assertEqual(response.status, 200)
            with self.assertRaises(HTTPError) as caught:
                call("/events", token="invalid")
            self.assertEqual(caught.exception.code, 401)
            with call("/events", event()) as response:
                self.assertEqual(response.status, 201)
            with call("/events", event()) as response:
                self.assertEqual(response.status, 200)
            with call("/alerts") as response:
                self.assertEqual(len(json.load(response)), 1)
            with call("/export.csv") as response:
                self.assertIn("SYN-0001", response.read().decode())
            with self.assertRaises(HTTPError) as caught:
                call("/events?limit=-1")
            self.assertEqual(caught.exception.code, 400)
            with self.assertRaises(HTTPError) as caught:
                call("/events", event(10))
            self.assertEqual(caught.exception.code, 409)
        finally:
            server.shutdown()
            server.server_close()
            thread.join()


if __name__ == "__main__":
    unittest.main()
