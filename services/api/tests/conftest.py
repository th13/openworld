import pytest
from api.server import server, io

@pytest.fixture
def t_server():
    return server

@pytest.fixture
def t_io():
    return io