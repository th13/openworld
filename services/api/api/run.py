import os
from src.api import server

if __name__ == '__main__':
    server.run(host=os.environ['API_HOST'], 
               port=int(os.environ['API_PORT']))