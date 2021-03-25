from motor.motor_asyncio import AsyncIOMotorClient

from source.loggers import default_logger
from source import settings


client:AsyncIOMotorClient = AsyncIOMotorClient(settings.MONGO_URL)

db = client[settings.MONGO_DATABASE]

default_logger.info(f'MongoDB database "{settings.MONGO_DATABASE}" created')
