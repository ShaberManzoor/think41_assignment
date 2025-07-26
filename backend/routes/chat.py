from fastapi import APIRouter, HTTPException
from models import ChatRequest, ChatResponse, Message, ConversationSession
from db import db
from datetime import datetime
import uuid
from utils.llm import get_llm_response

router = APIRouter()

@router.post("/api/chat", response_model=ChatResponse)
async def chat_api(request: ChatRequest):
    # Generate new session_id if not provided
    session_id = request.session_id or str(uuid.uuid4())

    # Check if session exists
    session = await db["sessions"].find_one({"session_id": session_id})
    
    if not session:
        # If session doesn't exist, create a new one
        session_data = {
            "user_id": request.user_id,
            "session_id": session_id,
            "started_at": datetime.utcnow(),
            "messages": []
        }
        await db["sessions"].insert_one(session_data)

    # Create the user message
    user_msg = {"role": "user", "content": request.message}

    # Add user message to the session
    await db["sessions"].update_one(
        {"session_id": session_id},
        {"$push": {"messages": user_msg}}
    )

    # Fetch full session to build LLM prompt
    session = await db["sessions"].find_one({"session_id": session_id})
    prompt = "You are a helpful assistant for an e-commerce website. Use the conversation below to understand the context and assist the user appropriately.\n\n"

    for message in session["messages"]:
        prompt += f"{message['role'].capitalize()}: {message['content']}\n"

    prompt += "Assistant:"

    # Get LLM response from Groq
    try:
        ai_reply = await get_llm_response(prompt)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"LLM Error: {str(e)}")

    # Create assistant message
    ai_msg = {"role": "assistant", "content": ai_reply}

    # Save assistant message
    await db["sessions"].update_one(
        {"session_id": session_id},
        {"$push": {"messages": ai_msg}}
    )

    # Return response
    return ChatResponse(session_id=session_id, response=ai_reply)

# Optional: Fetch all sessions for a user
@router.get("/api/sessions/{user_id}")
async def get_sessions_for_user(user_id: str):
    sessions = await db["sessions"].find({"user_id": user_id}).to_list(length=100)
    return sessions
