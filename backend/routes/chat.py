# backend/routes/chat.py
from fastapi import APIRouter, HTTPException
from models import ChatRequest, ChatResponse
from db import db
from utils.ai_response import get_ai_response
from datetime import datetime
import uuid

router = APIRouter()

@router.post("/api/chat", response_model=ChatResponse)
async def chat_api(request: ChatRequest):
    # Generate or reuse session_id
    session_id = request.session_id or str(uuid.uuid4())

    # Fetch session or create new
    session = await db["sessions"].find_one({"session_id": session_id})
    if not session:
        # Create a new session
        session_data = {
            "user_id": request.user_id,
            "session_id": session_id,
            "started_at": datetime.utcnow(),
            "messages": []
        }
        await db["sessions"].insert_one(session_data)

    # User message
    user_msg = {"role": "user", "content": request.message}
    
    # AI response
    ai_content = get_ai_response(request.message)
    ai_msg = {"role": "assistant", "content": ai_content}

    # Update session messages
    await db["sessions"].update_one(
        {"session_id": session_id},
        {"$push": {"messages": {"$each": [user_msg, ai_msg]}}}
    )

    return ChatResponse(session_id=session_id, response=ai_content)
