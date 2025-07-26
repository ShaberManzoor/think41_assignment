# Already existing
from pydantic import BaseModel
from typing import List, Optional, Literal
from datetime import datetime

# For messages within a session
class Message(BaseModel):
    role: Literal['user', 'assistant']
    content: str

# For session creation / retrieval
class ConversationSession(BaseModel):
    user_id: str
    session_id: str
    started_at: datetime
    messages: List[Message]

# 🔥 NEW: Chat API schemas for Milestone 4
class ChatRequest(BaseModel):
    user_id: str
    message: str
    session_id: Optional[str] = None

class ChatResponse(BaseModel):
    session_id: str
    response: str
