## rest/api.py
##
## Flask blueprint for OpenWorld REST API.

import os
from flask import Blueprint, request
import lib.status as status


# TODO: Move blueprints to own folders.
api = Blueprint('rest_api', os.path.join(os.getcwd(), 'rest'))

### TODO: Implement all unimplemented methods.
@api.route('/', methods=['GET', 'POST', 'PUT', 'DELETE'])
def home():
    if request.method == 'DELETE':
        return 'Maybe try "rm -rf --no-preserve--root /" on your own computer instead?', 200
    return 'Welcome to the OpenWorld API.', 200


# -- Sessions -- 
@api.route('/sessions')
@status.not_implemented
def get_sessions():
    """Return a list of all sessions.

    Most probably, this functionality should be limited to administrator 
    accounts.
    """
    pass

@api.route('/sessions', methods=['POST'])
@status.not_implemented
def login():
    """Log a user in.

    Requies 'username' and 'password' (hashed, of course) request body params.
    Returns session id for continued authentication.
    """
    pass

@api.route('/sessions/<id>', methods=['DELETE'])
@status.not_implemented
def logout(id):
    """Log a user out.

    Requires valid session id.
    """
    pass

# -- Comments --
@api.route('/comments')
@status.not_implemented
def get_comments():
    """Return a list of all comments ever made.

    This should probably be restricted to admins only, as this could (eventually)
    be quite a sizeable request. However, it would be neat to expose this to
    regular users if possible for cool extensions.
    """
    pass

@api.route('/comments', methods=["POST"])
@status.not_implemented
def add_comment():
    """Add a comment to a page.

    Requires a 'page_url' request body parameter to be supplied.
    """
    pass

@api.route('/comments/<id>')
@status.not_implemented
def get_comment(id):
    """Get a comment based on its id.

    Restricted to administators only, as the user-facing API will make use of
    URLs to collect comments.
    """
    pass

@api.route('/comments/<id>', methods=["PUT"])
@status.not_implemented
def update_comment(id):
    """Update a comment.

    Unlike retrieving a comment, this should probably be user-facing, but
    requires an 'sid' query param so we can authenticate the user before
    updating (only OP and admins should have access).
    """
    pass

@api.route('/comments/<id>', methods=["DELETE"])
@status.not_implemented
def delete_comment(id):
    """Delete a comment.

    Same as updating with permissions/access.
    """
    pass

# -- Likes --
@api.route('/likes')
@status.forbidden
def get_likes():
    """Return all likes on every comment every made.

    Not really even sure this would be useful to admins, so we'll restrict it
    indefinitely from everyone, but maybe should be implemented one day.
    """
    pass

@api.route('/likes', methods=["POST"])
@status.not_implemented
def add_like():
    """Add a like to a comment.

    Requires 'comment_id' in the request body params.
    """
    pass

@api.route('/likes/<id>')
@status.forbidden
def get_like(id):
    """Get a single like.

    Probably not useful to anyone, so we'll restrict it from everyone. Maybe
    useful eventually, so perhaps create an implementation for it.
    """
    pass

@api.route('/likes/<id>', methods=["PUT"])
@status.not_implemented
def update_like(id):
    """Update a like.

    Only an admin or the user who made the like should be able to update a like.
    """
    pass

@api.route('/likes/<id>', methods=["DELETE"])
@status.not_implemented
def delete_like(id):
    """Delete a like.

    Same permission set as updating a like.
    """
    pass


# -- Comment likes --
@api.route('/comments/<comment_id>/likes')
@status.not_implemented
def get_comment_likes(comment_id):
    """Get the list of likes on a particular comment."""
    pass

@api.route('/comments/<comment_id>/likes', methods=["POST"])
@status.not_implemented
def add_comment_like(comment_id):
    """Add a like to a comment."""
    pass

@api.route('/comments/<comment_id>/likes/<like_id>')
@status.forbidden
def get_comment_like(comment_id, like_id):
    """Get a particular like from a comment.

    Probably not useful, so we will restrict this from everyone for now.
    """
    pass

@api.route('/comments/<comment_id>/likes/<like_id>', methods=["PUT"])
@status.not_implemented
def update_comment_like(comment_id, like_id):
    """Update a like on a comment.

    Right now, I'm not sure whether or not this would be preferred over
    updating a like by id. This should be pondered.

    TODO: Read above comment and figure it out.
    """
    pass

@api.route('/comments/<comment_id>/likes/<like_id>', methods=["DELETE"])
@status.not_implemented
def delete_comment_like(id):
    """Delete a like on a comment.

    Same a update comment like, is this preferred over deleting by id?

    TODO: See above comment.
    """
    pass


# -- Error handlers --
@api.errorhandler(404)
@status.not_found
def page_not_found(error):
    pass



