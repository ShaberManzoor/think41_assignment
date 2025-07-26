from pydantic import BaseModel, Field
from typing import List, Optional

class Message(BaseModel):
    role: str  # "user" or "assistant"
    content: str

class ChatSession(BaseModel):
    user_id: str
    messages: List[Message] = []