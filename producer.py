"""Genera únicamente pacientes y mediciones ficticios; carga secuencial moderada."""
import argparse
import json
import os
import random
import time
import uuid
from datetime import datetime, timezone
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError


def generate(count, patients, seed):
    rng = random.Random(seed)
    for i in range(count):
        # Ciclo de tres estados garantiza datos para la demostración inicial.
        yield {"event_id": str(uuid.uuid4()), "patient_id": f"SYN-{i % patients + 1:04}", "timestamp": datetime.now(timezone.utc).isoformat(), "heart_rate": rng.randint(55, 130), "spo2": rng.randint(85, 100), "signal_score": [10, 50, 90][i % 3]}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--url", help="Ejemplo: http://127.0.0.1:8080/events; sin URL emite JSONL")
    parser.add_argument("--count", type=int, default=30)
    parser.add_argument("--patients", type=int, default=5)
    parser.add_argument("--rate", type=float, default=2)
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()
    if not 1 <= args.patients <= 9999 or not 1 <= args.count <= 10000 or not 0 < args.rate <= 20:
        parser.error("patients: 1..9999; count: 1..10000; rate: >0 y <=20")
    token = os.environ.get("API_TOKEN", "")
    if args.url and len(token) < 16:
        parser.error("Configura API_TOKEN con al menos 16 caracteres")
    failed = 0
    for event in generate(args.count, args.patients, args.seed):
        if not args.url:
            print(json.dumps(event))
            continue
        request = Request(args.url, data=json.dumps(event).encode(), headers={"Content-Type": "application/json", "Authorization": "Bearer " + token}, method="POST")
        try:
            with urlopen(request, timeout=10) as response:
                print(response.status, response.read().decode())
        except (HTTPError, URLError, TimeoutError):
            failed += 1
            print("ERROR de envío", event["event_id"])
        time.sleep(1 / args.rate)
    if failed:
        raise SystemExit(f"Fallaron {failed} eventos")


if __name__ == "__main__":
    main()
