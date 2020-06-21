from pydantic import BaseModel
from typing import List, Any
from datetime import datetime

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


class DirectCMessageModel(BaseModel):
    sender: str
    receiver: str
    messages: List[MessageListModel]


class MessageInPacketModel(BaseModel):
    content_type: str
    content: str


class DirectMessagePacket(BaseModel):
    receiver: str
    message: MessageInPacketModel


# class MessagePacket(BaseModel):
#     token: str
#     packet_type: str
#     content: DirectMessagePacket
