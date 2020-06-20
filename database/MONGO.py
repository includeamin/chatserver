from pymongo import MongoClient
from settings.Settings import database_settings

database = MongoClient(database_settings.DATABASE_URL)

direct_chat = database.get_database(database_settings.DIRECT_CHAT_COLLECTION)
group_chat_collection = database.get_database(database_settings.GROUPS_CHAT_COLLECTION)
channel_chat_collection = database.get_database(database_settings.CHANNEL_CHAT_COLLECTION)
signaling_collection = database.get_database(database_settings.SIGNALING_COLLECTION)
