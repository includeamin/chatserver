from pydantic import BaseModel
from typing import Any
from models.Chat import DirectMessagePacket


class HeadersModel(BaseModel):
    HTTP_TOKEN: str


class ServerResponse(BaseModel):
    message: Any
    code: int


class MessagePacket(BaseModel):
    token: str
    packet_type: str
    content: DirectMessagePacket


class DirectMessageEmitModel(BaseModel):
    sender: str
    packet_type: str
    content: DirectMessagePacket


class PacketTypes(BaseModel):
    direct_message: str = "direct_message"


packets_types = PacketTypes()
