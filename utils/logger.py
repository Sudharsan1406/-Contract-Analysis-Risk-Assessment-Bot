import json
import os
from datetime import datetime

LOG_DIR = "logs"
LOG_FILE = "logs/audit_log.json"


def _ensure_log_file():
    os.makedirs(LOG_DIR, exist_ok=True)
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, "w") as f:
            json.dump([], f)


def log_event(event_type: str, data: dict):
    """
    Append an event to audit log.
    """
    _ensure_log_file()

    log_entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "event": event_type,
        "data": data
    }

    with open(LOG_FILE, "r+") as f:
        logs = json.load(f)
        logs.append(log_entry)
        f.seek(0)
        json.dump(logs, f, indent=2)
