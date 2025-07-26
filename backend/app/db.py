from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId

client = None
db = None

async def init_db():
    global client, db
    client = AsyncIOMotorClient("mongodb://localhost:27017")
    db = client.chatbot