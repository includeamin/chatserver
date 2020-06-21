from socketio.asyncio_namespace import AsyncNamespace
from logging import info
from authentication.JWT import JWT
from WebSocket.utils import get_headers
from models.Websocket import ServerResponse


class ChatNameSpace(AsyncNamespace):
    async def on_connect(self, environ, *args, **kwargs):
        headers = get_headers(args)
        user_id = JWT.validate(headers.HTTP_TOKEN)
        # user_id = headers.HTTP_TOKEN
        session_id = environ
        self.enter_room(session_id, user_id, namespace=self.namespace)
        await self.emit('SERVER_RESPONSE', ServerResponse(message='welcome!', code=0).dict())
        info(f"{user_id} is connected")

    def on_disconnect(self, environ, *args, **kwargs):
        info(f"user disconnected")

    def on_message(self, data):
        print(data)

    def on_delivered(self):
        pass

    def on_seen(self):
        pass
