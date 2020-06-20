from fastapi import FastAPI
from WebSocket.SocketIo import app as websocket_app

app = FastAPI()
app.mount("/", websocket_app)
