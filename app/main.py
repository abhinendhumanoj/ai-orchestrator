from fastapi import FastAPI
from app.api import orchestrate
from fastapi.middleware.cors import CORSMiddleware

# Create FastAPI app
app = FastAPI(title="AI Tutor Orchestrator", version="0.1.0")

# ✅ Add CORS middleware so React frontend can call backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React runs on 3000
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "AI Tutor Orchestrator API is running"}

# Include orchestrator router
app.include_router(orchestrate.router, prefix="/api")
