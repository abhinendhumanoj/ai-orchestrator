import os
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    print("❌ ERROR: OPENAI_API_KEY not found in .env")
else:
    print("✅ API Key loaded successfully")

# Initialize client
client = OpenAI(api_key=api_key) if api_key else None
router = APIRouter()

class OrchestrateRequest(BaseModel):
    user_message: str


@router.post("/orchestrate")
def orchestrate(req: OrchestrateRequest):
    if not client:
        raise HTTPException(status_code=500, detail="API key missing or invalid")

    # Step 1: Detect user intent
    intent_prompt = f"""
    Analyze the following user request and classify it into one of these categories:
    - tutor (for explanation or teaching)
    - summarizer (for summaries or simplifications)
    - quiz (if the user is asking for quiz questions)
    Return ONLY one word: tutor, summarizer, or quiz.

    User message: "{req.user_message}"
    """

    detect = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "system", "content": "You are an intent detection assistant."},
                  {"role": "user", "content": intent_prompt}],
        temperature=0
    )

    mode = detect.choices[0].message.content.strip().lower()

    # Step 2: Choose system prompt based on detected mode
    if mode == "tutor":
        system_prompt = "You are an intelligent tutor. Explain clearly and step by step."
    elif mode == "summarizer":
        system_prompt = "You are a summarizer. Provide short, concise summaries."
    elif mode == "quiz":
        system_prompt = "You are a quiz maker. Generate 3-5 interesting questions with answers."
    else:
        system_prompt = "You are a helpful AI assistant."

    # Step 3: Generate final response
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": req.user_message},
        ],
        temperature=0.7
    )

    final_answer = completion.choices[0].message.content

    return {
        "detected_mode": mode,
        "answer": final_answer
    }
