# utils/data_loader.py
from pathlib import Path
import json
from typing import Any, Dict, Optional

_DATA: Dict[str, Any] | None = None

def _load() -> Dict[str, Any]:
    global _DATA
    if _DATA is None:
        here = Path(__file__).resolve().parent
        path = (here / ".." / "data" / "test_data.json").resolve()
        with path.open("r", encoding="utf-8") as f:
            _DATA = json.load(f)
    return _DATA

def get_all() -> Dict[str, Any]:
    return _load()

def get(section: Optional[str] = None, default: Any = None) -> Any:
    data = _load()
    if not section:
        return data
    cur: Any = data
    for part in section.split("."):
        if isinstance(cur, dict) and part in cur:
            cur = cur[part]
        else:
            return default
    return cur
