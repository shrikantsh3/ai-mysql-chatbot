import os
from fastapi import FastAPI
from pydantic import BaseModel
# import your AI modules here (e.g., google-generativeai, langchain)

app = FastAPI(
    title="AI MySQL Chatbot API",
    description="FastAPI backend connected to WordPress"
)

# Define the structure of incoming data from WordPress
class ChatRequest(BaseModel):
    message: str

@app.get("/")
def home():
    return {"status": "AI API is running smoothly"}

@app.post("/api/chat")
async def chat(payload: ChatRequest):
    user_message = payload.message
    
    # --- Your AI / LangChain Logic Goes Here ---
    # response = your_ai_model_generate(user_message)
    ai_response = f"FastAPI received: {user_message}"
    # -------------------------------------------
    
    return {"response": ai_response}

if __name__ == "__main__":
    import uvicorn
    # Render dynamically assigns a PORT environment variable
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("app:app", host="0.0.0.0", port=port, reload=False)