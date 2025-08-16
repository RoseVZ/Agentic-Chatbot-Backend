from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from fastapi.middleware.cors import CORSMiddleware

from model import Me  

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
me = Me()

class Message(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    message: str
    history: List[Message] = []

@app.get("/ping")
def ping():
    return {"status": "ok"}

@app.post("/chat")
async def chat_endpoint(request: ChatRequest):
    # Convert history to the format your Me.chat() expects
    history_formatted = [{"role": m.role, "content": m.content} for m in request.history]
    # Get the reply from your Me.chat() method
    reply = me.chat(request.message, history_formatted)
    # Return the reply in a JSON response
    return {"reply": reply}
