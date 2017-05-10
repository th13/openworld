import os
from flask import Flask, Blueprint
from functools import wraps

config = {
    'host': os.environ['API_HOST'],
    'port': int(os.environ['API_PORT'])
}

# TODO: Move blueprints to own folders.
api = Blueprint('api', __name__)

def not_implemented(route_fn):
    """Flask route decorator for routes that haven't been implemented yet."""
    @wraps(route_fn)
    def decorated(*args, **kwargs):
        return 'This functionality has not been implemented yet.', 501
    return decorated

### TODO: Implement all unimplemented methods.
@api.route('/')
def api_home():
    return 'Welcome to the OpenWorld API.', 200

@api.route('/login', methods=['POST'])
@not_implemented
def login():
    pass

@api.route('/logout', methods=['POST'])
@not_implemented
def logout():
    pass

@api.errorhandler(404)
def page_not_found(error):
    pass



server = Flask(__name__)
server.register_blueprint(api, url_prefix='/api')

@server.route('/')
def root():
    """Everyone loves easter eggs."""
    return 'http://www.youtube.com/watch?v=e69-GO4bYLM', 418


if __name__ == '__main__':
    server.run(host=config['host'], port=config['port'])
