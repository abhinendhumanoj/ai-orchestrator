# app/tools/flashcards.py
from typing import List, Dict

def flashcards_mock(topic: str, count: int = 5) -> Dict:
    """
    Mock flashcard generator: returns list of simple Q/A pairs.
    """
    cards: List[Dict] = []
    short_topic = topic.strip()[:50]
    for i in range(count):
        q = f"What is concept {i+1} about {short_topic}?"
        a = f"Answer {i+1} (mock)."
        cards.append({"question": q, "answer": a})
    return {"topic": short_topic, "count": count, "cards": cards, "meta": {"method": "mock"}}
