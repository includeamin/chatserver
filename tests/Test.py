import socketio

base_url = 'http://localhost:3000'
token = 'aminjamal'
sio = socketio.Client()
sio.connect(
    f'{base_url}', namespaces="/chat", headers={"token": "aminjamal"})


@sio.on("SERVER_RESPONSE", namespace="/chat")
def server_response(data):
    print(data)


message_pack = {
    'token': token
}

while True:
    message = input("MESSAGE: ")
    user_id = input("USER_ID: ")
