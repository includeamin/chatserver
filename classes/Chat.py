from models.Chat import *
from database.MONGO import direct_chat_collection
from models.Websocket import MessagePacket


class ChatActions:
    @staticmethod
    async def add_direct_message(packet: MessagePacket):
        direct_chat_collection.update_one({"sender": packet.token, "receiver": packet.content.receiver},
                                          {"$addToSet": {
                                              "messages": MessageListModel(**packet.content.message.dict()).dict()
                                          }}, upsert=True)
        # todo : check updated or not

    @staticmethod
    def process_packet(packet: MessagePacket):
        if packet.packet_type == 'direct_message':
            return ChatActions.add_direct_message(packet)
        else:
            return 'not support at moment'
