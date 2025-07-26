from fastapi import APIRouter, Body
from models import Message, ChatSession
from db import db
from uuid import uuid4
import httpx
import os

chat_router = APIRouter()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"

@chat_router.post("/chat")
async def chat(user_id: str = Body(...), message: str = Body(...), conversation_id: Optional[str] = Body(None)):
    session = None

    if conversation_id:
        session = await db.sessions.find_one({"_id": conversation_id})
    
    if not session:
        conversation_id = str(uuid4())
        session = {
            "_id": conversation_id,
            "user_id": user_id,
            "messages": []
        }
        await db.sessions.insert_one(session)

    user_msg = {"role": "user", "content": message}
    session["messages"].append(user_msg)

    # Call LLM (Groq or mock)
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(
                GROQ_API_URL,
                headers={"Authorization": f"Bearer {GROQ_API_KEY}"},
                json={
                    "model": "mixtral-8x7b-32768",
                    "messages": session["messages"][-10:],
                    "temperature": 0.7
                }
            )
            data = response.json()
            ai_response = data["choices"][0]["message"]
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    session["messages"].append(ai_response)
    await db.sessions.update_one({"_id": conversation_id}, {"$set": {"messages": session["messages"]}})

    return {"conversation_id": conversation_id, "messages": session["messages"]}


@chat_router.get("/history/{user_id}")
async def get_conversations(user_id: str):
    sessions = await db.sessions.find({"user_id": user_id}).to_list(100)
    return sessions