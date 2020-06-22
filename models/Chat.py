from bson import ObjectId
from pydantic import BaseModel, Field
from typing import List, Any
from datetime import datetime
from models.Websocket import ServerMessagePacket

statuses = [
    "sent"
    "seen",
    "delivered"
]

content_types = [
    "text"
    # ,
    # "image",
    # "video",
    # "audio",
    # "text/video",
    # "text/image",
    # "text/audio"
]

packet_types = [
    "direct"
    # ,
    # "group",
    # "channel"
]


class MessageListModel(BaseModel):
    status: str = 'sent'
    content_type: str
    content: str
    create_at: datetime = datetime.now()


class DirectMessageModel(BaseModel):
    sender: str
    receiver: str
    messages: List[MessageListModel]


class MessageInPacketModel(BaseModel):
    content_type: str
    content: str


class ChatHistoryModel(ServerMessagePacket):
    status: str = 'sent'


class DirectMessagePacket(BaseModel):
    receiver: str
    message: MessageInPacketModel


class SubscribeModel(BaseModel):
    user_id: str
    type: str = 'user'


class GroupDatabaseModel(BaseModel):
    name: str
    owner: str
    create_at: datetime = datetime.now()
    subscribes: List[SubscribeModel] = []


class CreateGroupBodyModel(BaseModel):
    name: str


class GroupMessages(BaseModel):
    sender: str
    content_type: str
    content: Any
    reply_to: str
    create_at: datetime = datetime.now()
