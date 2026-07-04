import os
import sys

import pytest

# Add app directory to Python path so `from app import app` works from repo root.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import app  # noqa: E402


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as test_client:
        yield test_client


def test_home_endpoint(client):
    response = client.get("/")

    assert response.status_code == 200

    data = response.get_json()
    assert data["message"] == "Hello DevOps Engineer!"
    assert data["environment"] == "development"
    assert data["status"] == "healthy"
