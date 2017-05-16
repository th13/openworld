import os
from server import server, socketio
import ws.api

# This is mostly an easter egg.
@server.route('/', methods=['GET', 'POST', 'PUT', 'DELETE'])
def root():
    pass

if __name__ == '__main__':
    socketio.run(server,
           host=os.environ['API_HOST'], 
           port=int(os.environ['API_PORT']))