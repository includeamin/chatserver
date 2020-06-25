from bson import ObjectId
from pydantic import BaseModel, Field, validator
from typing import List, Any
from datetime import datetime
from models.Websocket import ServerMessagePacket
from fastapi import HTTPException

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

valid_create_bys = [
    "admin",
    "user"
]

valid_create_for_names = [
    'live_class'
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
    user_name: str
    type: str = 'user'


class CreateForModel(BaseModel):
    id: str
    name: str

    @validator('name')
    def name_validator(cls, v):
        if v not in valid_create_for_names:
            raise HTTPException(detail=f'invalid name for create for,{valid_create_for_names}', status_code=400)


class GroupDatabaseModel(BaseModel):
    name: str
    owner: str
    create_by: str
    create_for: CreateForModel = None
    create_at: datetime = datetime.now()
    subscribes: List[SubscribeModel] = []

    @validator('create_by')
    def create_by_validator(cls, v):
        if v not in valid_create_bys:
            raise HTTPException(detail=f"invalid create_by,{valid_create_bys}", status_code=400)
        return v


class GetUserSubscribes(BaseModel):
    group_id: List[str]


class AdminCreateGroupBodyModel(BaseModel):
    name: str
    create_for: CreateForModel = None


class AdminCreateGroupResponseModel(BaseModel):
    group_id: str


class CreateGroupBodyModel(BaseModel):
    name: str


class GroupMessages(BaseModel):
    sender: str
    content_type: str
    content: Any
    reply_to: str
    create_at: datetime = datetime.now()
