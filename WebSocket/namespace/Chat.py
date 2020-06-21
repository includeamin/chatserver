from socketio.asyncio_namespace import AsyncNamespace
from logging import info
from authentication.JWT import JWT
from WebSocket.utils import get_headers
from models.Websocket import *
from classes.Chat import ChatActions, DirectCMessageModel
from settings.Settings import events_names


class ChatNameSpace(AsyncNamespace):
    async def on_connect(self, environ, *args, **kwargs):
        headers = get_headers(args)
        user_id = JWT.validate(headers.HTTP_TOKEN)
        session_id = environ
        self.enter_room(session_id, user_id, namespace=self.namespace)
        await self.emit(events_names.SERVER_RESPONSE, ServerResponse(message='welcome!', code=0).dict(), room=user_id)

    def on_disconnect(self, environ, *args, **kwargs):
        info(f"user disconnected")

    async def on_DIRECT_MESSAGE(self, data, *args, **kwargs):
        packet = MessagePacket(**args[0])
        user_id = JWT.validate(packet.token)
        if packet.packet_type == packets_types.direct_message:
            data = DirectMessageEmitModel(sender=user_id, content=packet.content, packet_type=packet.packet_type)
            await self.emit(events_names.DIRECT_MESSAGE, data.dict(), room=packet.content.receiver)
            await ChatActions.add_direct_message(packet)
        else:
            await self.emit(events_names.SERVER_RESPONSE,
                            ServerResponse(message="at the moment, only direct message supported", code=1))

    def on_delivered(self):
        pass

    def on_seen(self):
        pass
