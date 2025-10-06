import os
from dotenv import load_dotenv

from fastapi import FastAPI
from typing import Dict
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()

app = FastAPI(
    title="My FastAPI App",
    description="A simple FastAPI application",
    version="1.0.0"
)

@app.get("/")
async def read_root() -> Dict[str, str]:
    """
    Root endpoint that returns a joke message.
    """
    oai_client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
    completion = oai_client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
        {"role": "system", "content": "You are a helpful comedian."},
        {"role": "user", "content": "Tell me a joke."},
    ],
    )
    return {"message": completion.choices[0].message.content}

@app.get("/health")
async def health_check() -> Dict[str, str]:
    """
    Health check endpoint.
    """
    return {"status": "healthy"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None) -> Dict:
    """
    Get an item by ID with optional query parameter.
    """
    return {"item_id": item_id, "q": q}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
