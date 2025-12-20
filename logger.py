import datetime

def log(message: str):
    ts = datetime.datetime.utcnow().isoformat()
    return f"[{ts}] {message}"
