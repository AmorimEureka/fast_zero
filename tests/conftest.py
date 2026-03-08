import pytest
from fastapi.testclient import TestClient

from fast_zero.app import app


@pytest.fixture
def client_arranj():
    return TestClient(app)
