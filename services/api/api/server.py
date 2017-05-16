import os
from flask import Flask
from flask_socketio import SocketIO

server = Flask(__name__)
server.config['SECRET_KEY'] = '5up3r_53cr3t_k3y'

socketio = SocketIO(server)



