from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from llm_api import generate_response
from pydantic import BaseModel
import uvicorn
import os

app = FastAPI()
MAX_INPUT_LENGTH = 32


origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "http://localhost:8000",
    "http://0.0.0.0:8000",
    "*", 
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, OPTIONS, etc.)
    allow_headers=["*"],  
)

# Debugging: Check if CORS is applied properly
@app.middleware("http")
async def log_request(request, call_next):
    response = await call_next(request)
    print("🔹 CORS Headers:", response.headers)
    return response

class ChatRequest(BaseModel):
    message: str

# Association Information
@app.get("/association")
def get_association():
    return {
        "name": "Association XYZ",
        "mission": "Promouvoir l'innovation et la collaboration.",
        "history": "Fondée en 2023 pour connecter les passionnés de technologie."
    }

# Partners Information
@app.get("/partners")
def get_partners():
    return {
        "partners": [
            {"name": "TechCorp", "type": "Technology"},
            {"name": "InnoSoft", "type": "Software"},
            {"name": "GreenFuture", "type": "Environment"}
        ]
    }

# Events Information
@app.get("/events")
def get_events():
    return {
        "events": [
            {"title": "Conférence Tech 2025", "date": "2025-03-15", "location": "Paris"},
            {"title": "Hackathon Innov'Nation", "date": "2025-06-20", "location": "Lyon"},
            {"title": "Forum de l'Innovation", "date": "2025-09-10", "location": "Marseille"}
        ]
    }

# Chatbot Interaction
@app.post("/chatbot")
def chat_with_bot(request: ChatRequest):
    try:
        response = generate_response(request.message)
        return {"response": response}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

# Health Check
@app.get("/")
def root():
    return {"message": "Association API is running"}


def validate_length_prompt(prompt: str):
    if len(prompt) >= MAX_INPUT_LENGTH:
        raise HTTPException(
            status_code=400,
            detail=f"Input is too long.Must be under 50 tokens"
        )
    
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
