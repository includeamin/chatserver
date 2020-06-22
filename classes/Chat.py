from models.Chat import *
from database.MONGO import direct_chat_collection
from models.Websocket import ServerMessagePacket
from models.Chat import ChatHistoryModel


class ChatActions:
    @staticmethod
    async def add_direct_message(packet: ServerMessagePacket):
        chat_history = ChatHistoryModel(**packet.dict()).dict()
        await ChatActions.id_fix(chat_history)
        direct_chat_collection.insert_one(chat_history)

    @staticmethod
    async def id_fix(chat_history):
        chat_history["_id"] = ObjectId(chat_history['id'])
        chat_history.pop("id")
