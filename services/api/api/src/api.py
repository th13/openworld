import os
from flask import Flask, Blueprint
from functools import wraps
from lib.status import not_implemented, im_a_teapot


# TODO: Move blueprints to own folders.
api = Blueprint('api', __name__)



### TODO: Implement all unimplemented methods.
@api.route('/')
def api_home():
    return 'Welcome to the OpenWorld API.', 200


# -- Sessions -- 
@api.route('/sessions')
@not_implemented
def get_all_sessions():
    pass

@api.route('/sessions', methods=['POST'])
@not_implemented
def login():
    pass

@api.route('/sessions/<id>', methods=['DELETE'])
@not_implemented
def logout(id):
    pass

# -- Comments --
@api.route('/comments')
@not_implemented
def get_all_comments():
    pass

@api.route('/comments', methods=["POST"])
@not_implemented
def add_comment():
    pass

@api.route('/comments/<id>')
@not_implemented
def get_comment(id):
    pass

@api.route('/comments/<id>', methods=["PUT"])
@not_implemented
def update_comment(id):
    pass

@api.route('/comments/<id>', methods=["DELETE"])
@not_implemented
def delete_comment(id):
    pass

# -- Likes --
@api.route('/likes')
@not_implemented
def get_all_likes():
    pass

@api.route('/likes', methods=["POST"])
@not_implemented
def add_like():
    pass

@api.route('/likes/<id>')
@not_implemented
def get_like(id):
    pass

@api.route('/likes/<id>', methods=["PUT"])
@not_implemented
def update_like(id):
    pass

@api.route('/likes/<id>', methods=["DELETE"])
@not_implemented
def delete_like(id):
    pass


# -- Comment likes --
@api.route('/comments/<comment_id>/likes')
@not_implemented
def get_all_comment_likes(comment_id):
    pass

@api.route('/comments/<comment_id>/likes', methods=["POST"])
@not_implemented
def add_comment_like(comment_id):
    pass

@api.route('/comments/<comment_id>/likes/<like_id>')
@not_implemented
def get_comment_like(comment_id, like_id):
    pass

@api.route('/comments/<comment_id>/likes/<like_id>', methods=["PUT"])
@not_implemented
def update_comment_like(comment_id, like_id):
    pass

@api.route('/comments/<comment_id>/likes/<like_id>', methods=["DELETE"])
@not_implemented
def delete_comment_like(id):
    pass



# -- Error handlers --
@api.errorhandler(404)
def page_not_found(error):
    pass



server = Flask(__name__)
server.register_blueprint(api, url_prefix='/api')

@server.route('/')
@im_a_teapot
def root():
    pass

