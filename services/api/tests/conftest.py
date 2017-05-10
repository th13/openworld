import pytest
from api.src.api import server

@pytest.fixture
def app():
    return server