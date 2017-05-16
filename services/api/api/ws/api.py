from flask_socketio import send, emit
from server import socketio

@socketio.on('connect')
def on_connect():
    pass

@socketio.on('client_connected')
def on_client_connected(data):
    print(data)
    emit('yes', data)