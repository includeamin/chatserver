from fastapi import FastAPI
from WebSocket.SocketIo import app as websocket_app
from api.admin.Group import admin_group_routes
from fastapi.responses import UJSONResponse

app = FastAPI()
app.mount("/", websocket_app)
app.include_router(admin_group_routes, prefix='/group/admin', default_response_class=UJSONResponse)
