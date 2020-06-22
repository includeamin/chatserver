from pydantic import BaseModel
from typing import Any


class HeadersModel(BaseModel):
    HTTP_TOKEN: str


class ServerResponse(BaseModel):
    message: Any
    code: int


# class MessagePacket(BaseModel):
#     token: str
#     packet_type: str
#     content: DirectMessagePacket

class ClientMessagePacket(BaseModel):
    token: str
    packet_type: str
    receiver: str
    content_type: str
    content: Any


class ServerMessagePacket(BaseModel):
    id: str
    sender: str
    packet_type: str
    receiver: str
    content_type: str
    content: Any


class GroupMessagePacket(BaseModel):
    token: str
    group_id: str
    content_type: str
    content: str


class SeenPacket(BaseModel):
    pass


class PacketTypes(BaseModel):
    direct_message: str = "direct_message"


packets_types = PacketTypes()
