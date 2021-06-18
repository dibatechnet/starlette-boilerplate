from motor import motor_asyncio

from .settings import DATABASE_URL

mongo_client = motor_asyncio.AsyncIOMotorClient(DATABASE_URL)
