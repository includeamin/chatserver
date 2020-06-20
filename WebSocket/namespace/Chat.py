from socketio.asyncio_namespace import AsyncNamespace


class ChatNameSpace(AsyncNamespace):
    def on_connect(self, environ, *args, **kwargs):
        pass

    def on_disconnect(self):
        pass

    def on_message(self):
        pass

    def on_delivered(self):
        pass

    def on_seen(self):
        pass
