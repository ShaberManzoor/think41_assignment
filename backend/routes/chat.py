from fastapi import APIRouter, HTTPException
from models import ConversationSession
from db import db

router = APIRouter()

@router.post("/session")
async def create_session(session: ConversationSession):
    existing = await db["sessions"].find_one({"session_id": session.session_id})
    if existing:
        raise HTTPException(status_code=400, detail="Session already exists")
    await db["sessions"].insert_one(session.dict())
    return {"message": "Session created"}

@router.get("/session/{user_id}")
async def get_sessions(user_id: str):
    sessions = await db["sessions"].find({"user_id": user_id}).to_list(length=100)
    return sessions
