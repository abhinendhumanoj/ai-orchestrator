# app/tools/summarizer.py
from typing import Dict

def summarizer_mock(text: str, max_length: int = 200) -> Dict:
    """
    Mock summarizer: returns a structured dict (title, summary_text, meta).
    Replace this function body with an LLM call later.
    """
    snippet = text.strip()[:max_length]
    return {
        "title": f"Summary of: {snippet[:40]}",
        "summary_text": f"📄 {snippet}... (mock summary)",
        "meta": {"method": "mock", "length_est": len(snippet)}
    }