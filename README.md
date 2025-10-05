AI Orchestrator – Yophoria Innovation Challenge 2025
AI Orchestrator is an intelligent tutoring system developed for the Yophoria Innovation Challenge 2025. It provides an AI-driven interactive learning experience that allows users to ask academic or general questions and receive dynamic, step-by-step answers using OpenAI's GPT-4o-mini model.

🧠 Tech Stack
- Frontend:  React.js (Hosted on Vercel)
- Backend: FastAPI + Python (Hosted on Render)
- AI Engine: OpenAI GPT-4o-mini
- Communication:  RESTful API via Axios
  
🌐 Live URLs
Frontend:  https://ai-orchestrator-five.vercel.app
Backend:  https://ai-orchestrator-backend-ibmx.onrender.com

⚙️ Setup Instructions
🔹 Clone the repository
```bash
git clone https://github.com/abhinendhumanoj/ai-orchestrator.git
cd ai-orchestrator
```
🔹 Backend Setup
```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```
🔹 Frontend Setup
```bash
cd ai-tutor-frontend
npm install
npm start
```

📘 Project Summary
This AI Tutor Orchestrator allows users to engage in real-time Q&A interactions. The backend processes natural language input, classifies user intent, and generates intelligent responses using OpenAI’s GPT-4o-mini model.

👥 Team Members
• Abhinendhu Manoj
• Pradeepthi Givari
