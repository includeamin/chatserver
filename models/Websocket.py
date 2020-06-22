from pydantic import BaseModel
from typing import Any


class HeadersModel(BaseModel):
    HTTP_TOKEN: str


class PacketTypes(BaseModel):
    direct_message: str = "direct_message"
    group_message: str = 'gp_msg'


packets_types = PacketTypes()


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
    token: str
    sender: str


class SeenEmitPackage(BaseModel):
    receiver: str
