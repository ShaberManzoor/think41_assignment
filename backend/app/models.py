import uuid
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Enum
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
import enum

Base = declarative_base()

class ConversationSession(Base):
    __tablename__ = "conversation_sessions"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(Integer, nullable=True)
    started_at = Column(DateTime, server_default="NOW()")

class SenderEnum(enum.Enum):
    user = "user"
    ai = "ai"

class Message(Base):
    __tablename__ = "messages"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    conversation_id = Column(UUID(as_uuid=True), ForeignKey("conversation_sessions.id"))
    sender = Column(Enum(SenderEnum), nullable=False)
    content = Column(Text, nullable=False)
    timestamp = Column(DateTime, server_default="NOW()")
