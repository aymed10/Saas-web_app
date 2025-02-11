from fastapi import FastAPI, HTTPException
from llm_api import generate_response

app = FastAPI()
MAX_INPUT_LENGTH = 32

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