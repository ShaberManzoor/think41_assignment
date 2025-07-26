# backend/models.py
from pydantic import BaseModel
from typing import List, Literal
from datetime import datetime

class Message(BaseModel):
    role: Literal['user', 'assistant']
    content: str

class ConversationSession(BaseModel):
    user_id: str
    session_id: str
    started_at: datetime
    messages: List[Message]
