import socketio

base_url = 'http://localhost:3000'
token = input("token: ")
sio = socketio.Client()
sio.connect(
    f'{base_url}', namespaces="/chat", headers={"token": token})


@sio.on("SERVER_RESPONSE", namespace="/chat")
def server_response(data):
    print(data)


@sio.on("DIRECT_MESSAGE", namespace="/chat")
def direct_message(data):
    print(data)


message_pack = {
    'token': token,
    'packet_type': 'direct_message',
    'content': {
        'receiver': '',
        'message': {
            'content_type': 'txt',
            "content": ''
        }
    }
}

while True:
    message = input("MESSAGE: ")
    user_id = input("USER_ID: ")
    message_pack["content"]["receiver"] = user_id
    message_pack["content"]["message"]["content"] = message
    sio.emit("DIRECT_MESSAGE", message_pack, namespace="/chat")
