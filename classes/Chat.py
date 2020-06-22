from models.Chat import *
from database.MONGO import direct_chat_collection
from models.Websocket import ServerMessagePacket, SeenPacket
from models.Chat import ChatHistoryModel
from settings.Settings import permissions_settings
from fastapi import HTTPException


# TODO: add delivery mechanism on direct messaging

class ChatActions:
    class Public:
        @staticmethod
        async def create_group():
            if not permissions_settings.USER_CREATE_GROUP:
                raise HTTPException(detail="Permission Denied", status_code=406)

    class Shared:
        pass

    class Admin:
        pass

    @staticmethod
    async def add_direct_message(packet: ServerMessagePacket):
        chat_history = ChatHistoryModel(**packet.dict()).dict()
        await ChatActions.id_fix(chat_history)
        direct_chat_collection.insert_one(chat_history)

    @staticmethod
    async def id_fix(chat_history):
        chat_history["_id"] = ObjectId(chat_history['id'])
        chat_history.pop("id")

    @staticmethod
    async def seen(packet: SeenPacket):
        direct_chat_collection.update_many(
            {"$or": [{"$and": [{"sender": packet.token}, {"receiver": packet.sender}]},
                     {"$and": [{"sender": packet.sender}, {"receiver": packet.token}]}], "status": {"$ne": "seen"}},
            {"$set": {"status": 'seen'}})
