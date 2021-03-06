from socketio.asyncio_namespace import AsyncNamespace
from logging import info
from authentication.JWT import JWT
from WebSocket.utils import get_headers
from models.Websocket import *
from classes.Chat import ChatActions, ObjectId
from settings.Settings import events_names


class ChatNameSpace(AsyncNamespace):
    async def on_connect(self, environ, *args, **kwargs):
        # todo: subscribe to groups and channels
        headers = get_headers(args)
        user_id = JWT.validate(headers.HTTP_TOKEN)
        session_id = environ
        self.enter_room(session_id, user_id, namespace=self.namespace)
        await self.emit(events_names.SERVER_RESPONSE, ServerResponse(message='welcome!', code=0).dict(), room=user_id)

    def on_disconnect(self, environ, *args, **kwargs):
        info(f"user disconnected")

    async def on_direct_message(self, data, *args, **kwargs):
        packet = ClientMessagePacket(**args[0])
        user_id = JWT.validate(packet.token)
        if packet.packet_type == packets_types.direct_message:
            await self.direct_handler(packet, user_id)
        else:
            await self.emit(events_names.SERVER_RESPONSE,
                            ServerResponse(message="at the moment, only direct message supported", code=1))

    async def on_seen(self, data, *args, **kwargs):
        packet = SeenPacket(**args[0])
        user_id = JWT.validate(packet.token)
        packet.token = user_id
        await self.emit("msg_seen", {"msg": 'seen'}, room=packet.sender)
        await ChatActions.seen(packet)

    async def on_gp_msg(self, data, *args, **kwargs):
        pass

    async def direct_handler(self, packet, user_id):
        server_packet = ServerMessagePacket(id=str(ObjectId()), sender=user_id, receiver=packet.receiver,
                                            content_type=packet.content_type, content=packet.content,
                                            packet_type=packet.packet_type)
        await self.emit(events_names.DIRECT_MESSAGE, server_packet.dict(), room=server_packet.receiver)
        await ChatActions.add_direct_message(server_packet)
