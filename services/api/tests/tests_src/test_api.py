import pytest
from flask import request, url_for


def api_home_route_should_be_ok(client):
    assert client.get(url_for('api.home')).status_code == 200
    assert client.post(url_for('api.home')).status_code == 200
    assert client.put(url_for('api.home')).status_code == 200
    assert client.delete(url_for('api.home')).status_code == 200

