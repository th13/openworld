## test_api.py
##
## Run tests on the Flask REST API for OpenWorld.
##
## TODO: Update all *_should_be_not_implemented test cases with real tests once
## those functions are to be implemented.

import pytest
from flask import request, url_for
from api.lib.status import OK, NOT_IMPLEMENTED, NOT_FOUND, FORBIDDEN, IM_A_TEAPOT


def api_home_route_should_be_ok(client):
    assert client.get(url_for('api.home')).status_code    == OK
    assert client.post(url_for('api.home')).status_code   == OK
    assert client.put(url_for('api.home')).status_code    == OK
    assert client.delete(url_for('api.home')).status_code == OK

def get_sessions_should_be_not_implemented(client):
    assert client.get(url_for('api.get_sessions')).status_code == NOT_IMPLEMENTED

def login_should_be_not_implemented(client):
    assert client.post(url_for('api.login')).status_code == NOT_IMPLEMENTED

def logout_should_be_not_implemented(client):
    assert client.delete(url_for('api.logout', id='test')).status_code == NOT_IMPLEMENTED

def get_comments_should_be_not_implemented(client):
    assert client.get(url_for('api.get_comments')).status_code == NOT_IMPLEMENTED

def add_comment_should_be_not_implemented(client):
    assert client.post(url_for('api.add_comment')).status_code == NOT_IMPLEMENTED

def get_comment_should_be_not_implemented(client):
    assert client.get(url_for('api.get_comment', id='fake')).status_code == NOT_IMPLEMENTED

def update_comment_should_be_not_implemented(client):
    assert client.put(url_for('api.update_comment', id='fake')).status_code == NOT_IMPLEMENTED

def delete_comment_should_be_not_implemented(client):
    assert client.delete(url_for('api.delete_comment', id='fake')).status_code == NOT_IMPLEMENTED

def get_likes_should_be_forbidden(client):
    assert client.get(url_for('api.get_likes')).status_code == FORBIDDEN

def add_like_should_be_not_implemented(client):
    assert client.post(url_for('api.add_like')).status_code == NOT_IMPLEMENTED

def get_like_should_be_forbidden(client):
    assert client.get(url_for('api.get_like', id='fake')).status_code == FORBIDDEN

def update_like_should_be_not_implemented(client):
    assert client.put(url_for('api.update_like', id='fake')).status_code == NOT_IMPLEMENTED

def delete_like_should_be_not_implemented(client):
    assert client.delete(url_for('api.delete_like', id='fake')).status_code == NOT_IMPLEMENTED

def get_comment_likes_should_be_not_implemented(client):
    assert client.get(url_for('api.get_comment_likes', comment_id='fake')).status_code == NOT_IMPLEMENTED

def add_comment_like_should_be_not_implemented(client):
    assert client.post(url_for('api.add_comment_like', comment_id='fake')).status_code == NOT_IMPLEMENTED

def get_comment_like_should_be_forbidden(client):
    assert client.get(url_for('api.get_comment_like', comment_id='fake', like_id='fake')).status_code == FORBIDDEN

def update_comment_like_should_be_not_implemented(client):
    assert client.put(url_for('api.update_comment_like', comment_id='fake', like_id='fake')).status_code == NOT_IMPLEMENTED

def delete_comment_like_should_be_not_implemented(client):
    assert client.delete(url_for('api.delete_comment_like', comment_id='fake', like_id='fake')).status_code == NOT_IMPLEMENTED

def invalid_resource_should_be_not_found(client):
    assert client.get('/completely/invalid/resource').status_code == NOT_FOUND

def server_root_route_should_be_a_teapot(client):
    assert client.get(url_for('root')).status_code    == IM_A_TEAPOT
    assert client.post(url_for('root')).status_code   == IM_A_TEAPOT
    assert client.put(url_for('root')).status_code    == IM_A_TEAPOT
    assert client.delete(url_for('root')).status_code == IM_A_TEAPOT