from pydantic import BaseModel
from typing import Optional
from uuid import UUID

class ChatRequest(BaseModel):
    user_id: Optional[int] = None
    conversation_id: Optional[UUID] = None
    message: str

class ChatResponse(BaseModel):
    conversation_id: UUID
    response: str
