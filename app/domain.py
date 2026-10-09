"""Contrato portable entre la aplicación contenerizada y su evolución serverless."""
import math
import re
from datetime import datetime, timezone

FIELDS = {"event_id", "patient_id", "timestamp", "heart_rate", "spo2", "signal_score"}


def validate_event(event):
    if not isinstance(event, dict) or set(event) != FIELDS:
        raise ValueError("Se requieren exactamente: " + ", ".join(sorted(FIELDS)))
    if not isinstance(event["event_id"], str) or not re.fullmatch(r"[A-Za-z0-9-]{1,64}", event["event_id"]):
        raise ValueError("event_id inválido")
    if not isinstance(event["patient_id"], str) or not re.fullmatch(r"SYN-[0-9]{4}", event["patient_id"]):
        raise ValueError("patient_id debe ser ficticio y tener formato SYN-0001")
    try:
        instant = datetime.fromisoformat(event["timestamp"].replace("Z", "+00:00"))
        if instant.utcoffset() is None:
            raise ValueError("Falta zona horaria")
    except (ValueError, TypeError, AttributeError):
        raise ValueError("timestamp debe ser ISO 8601 con zona horaria") from None
    for field, maximum in [("heart_rate", 300), ("spo2", 100), ("signal_score", 100)]:
        value = event[field]
        if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value) or not 0 <= value <= maximum:
            raise ValueError(f"{field} fuera del contrato sintético")
    result = dict(event)
    result["timestamp"] = instant.astimezone(timezone.utc).isoformat()
    return result


def classify(event):
    # Índice artificial para pruebas de arquitectura; NO es una regla clínica.
    score = event["signal_score"]
    return "Crítico" if score >= 70 else "Precaución" if score >= 40 else "Normal"
