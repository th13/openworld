from flask import Flask

# TODO: Move these to env variables.
API_PORT = 5000
API_DEBUG = True

api = Flask(__name__)

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
    api.run('0.0.0.0', port=API_PORT, debug=API_DEBUG)


def not_implemented(route_fn):
    return 'This functionality has not been implemented yet', 501