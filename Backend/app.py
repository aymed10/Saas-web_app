from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from llm_api import generate_response
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

@app.get("/generate_response")
async def generate_response_api(prompt: str):
    validate_length_prompt(prompt)
    response = generate_response(prompt)
    return {"message": response}
    
def validate_length_prompt(prompt: str):
    if len(prompt) >= MAX_INPUT_LENGTH:
        raise HTTPException(
            status_code=400,
            detail=f"Input is too long.Must be under 12 tokens"
        )
    
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    uvicorn.run(app, host="0.0.0.0", port=port)
