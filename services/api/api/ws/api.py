## api.py
##
## Contains the SocketIO event-based API for OpenWorld.

from flask_socketio import send, emit
from server import socketio
from functools import wraps

auth_tokens = { 'abcdefg', 'bigisland' }

def authenticate(fn):
    """Decorator to require authentication for an event handler."""
    @wraps(fn)
    def wrapper(data):
        if not 'auth' in data or not data['auth'] in auth_tokens:
            emit('authentication_failed')
            return
        fn(data)
    return wrapper


@socketio.on('connect')
def on_connect():
    """Called when a client has connected to the server.

    Emits an authentication_requested event to tell the client they need to
    authenticate.
    """
    emit('authentication_requested')


@socketio.on('get_some_data')
@authenticate
def on_get_some_data(data):
    emit('here_is_data', { 'data': 'hi' })