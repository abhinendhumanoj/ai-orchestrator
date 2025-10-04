# app/tools/notes.py
from typing import Dict, List

def notes_mock(text: str, style: str = "outline") -> Dict:
    """
    Mock note maker returning a consistent structure.
    """
    kp: List[str] = [
        f"Key point 1: about {text[:20]}",
        "Key point 2: elaboration (mock)",
        "Key point 3: summary (mock)"
    ]
    return {
        "title": f"Notes: {text[:40]}",
        "style": style,
        "key_points": kp,
        "meta": {"method": "mock"}
    }
