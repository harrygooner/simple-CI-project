import os

import requests


def test_live_server_healthy():
    target_url = os.environ.get("APP_URL", "http://localhost:8080/")

    response = requests.get(target_url, timeout=5)
    assert response.status_code == 200

    data = response.json()
    assert data["status"] == "healthy"
    assert data["environment"] == "production"
