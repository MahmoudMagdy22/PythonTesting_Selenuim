# utils/helpers.py
from datetime import datetime, UTC
import random

def unique_email(prefix: str, domain: str) -> str:
    stamp = datetime.now(UTC).strftime("%Y%m%d%H%M%S")
    rand = random.randint(1000, 9999)
    return f"{prefix}.{stamp}{rand}@{domain}"
