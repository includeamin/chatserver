import socketio

base_url = 'http://localhost:3000'
token = input("token: ")
sio = socketio.Client()
sio.connect(
    f'{base_url}', namespaces="/chat", headers={"token": token})


@sio.on("server_response", namespace="/chat")
def server_response(data):
    print(data)


@sio.on("direct_message", namespace="/chat")
def direct_message(data):
    print(data)
    seen_package["sender"] = data['sender']
    seen_package["token"] = token
    sio.emit("seen", seen_package, namespace="/chat")


@sio.on("msg_seen", namespace="/chat")
def seen_msg(data):
    print("seen", data)


message_pack = {
    'token': token,
    "receiver": "",
    'packet_type': 'direct_message',
    'content_type': 'txt',
    "content": ''

}

seen_package = {
    "token": "",
    "sender": ""
}
while True:
    message = input("MESSAGE: ")
    user_id = input("USER_ID: ")
    message_pack["receiver"] = user_id
    message_pack["content"] = message
    sio.emit("direct_message", message_pack, namespace="/chat")
