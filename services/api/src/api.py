import os
from flask import Flask
from functools import wraps

config = {
    'host': os.environ['API_HOST'],
    'port': os.environ['API_PORT'],
    'debug': True if os.environ['API_DEBUG'] == 1 else False
}


api = Flask(__name__)


def not_implemented(route_fn):
    """Flask route decorator for routes that haven't been implemented yet."""
    @wraps(route_fn)
    def decorated(*args, **kwargs):
        return 'This functionality has not been implemented yet.', 501
    return decorated

### TODO: Implement all unimplemented methods.

@api.route('/')
def root():
    """Everyone loves easter eggs."""
    return 'http://www.youtube.com/watch?v=e69-GO4bYLM', 418

@api.route('/api')
@not_implemented
def api_home():
    pass

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


if __name__ == '__main__':
    api.run(host=config['host'], 
            port=config['port'], 
            debug=config['debug'])
