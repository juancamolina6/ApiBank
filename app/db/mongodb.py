from motor.motor_asyncio import AsyncIOMotorClient
from app.config.settings import settings

client = AsyncIOMotorClient(settings.MONGODB_URL)
db = client[settings.MONGODB_DB_NAME]
accounts_collection = db[settings.MONGODB_COLLECTION_NAME]