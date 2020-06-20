import socketio
from WebSocket.namespace.Chat import ChatNameSpace
from settings.Settings import database_settings

mgr = socketio.AsyncRedisManager(database_settings.REDIS_URL)
sio = socketio.AsyncServer(client_manager=mgr, async_mode='asgi')
sio.register_namespace(ChatNameSpace('/chat'))
app = socketio.ASGIApp(sio)
