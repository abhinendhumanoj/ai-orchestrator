from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import orchestrate

# ✅ Create FastAPI app
app = FastAPI(
    title="AI Tutor Orchestrator",
    version="0.1.0",
    description="Backend API for AI Tutor Orchestrator project",
)

# ✅ Enable CORS (for frontend connection)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",                     # Local React frontend
        "https://ai-tutor-frontend.onrender.com",    # Deployed frontend (Render)
        "https://ai-tutor-frontend.vercel.app",      # Optional Vercel deploy
        "*"                                          # Wildcard for temporary testing
    ],
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (POST, GET, etc.)
    allow_headers=["*"],  # Allow all headers
)

# ✅ Health check route
@app.get("/")
def read_root():
    return {"message": "AI Tutor Orchestrator API is running"}

# ✅ Main orchestration route (from app/api/orchestrate.py)
app.include_router(orchestrate.router, prefix="/api")
