import socketio

base_url = 'http://localhost:3000'
token = 'aminjamal'
sio = socketio.Client()
sio.connect(
    f'{base_url}', namespaces="/chat",headers={"data":"data"})
