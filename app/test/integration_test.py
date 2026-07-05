import os
import requests


BASE_URL = os.getenv("APP_BASE_URL", "http://127.0.0.1:8081")


def test_app_health():
    response = requests.get(f"{BASE_URL}/", timeout=10)

    assert response.status_code == 200

    data = response.json()
    assert data["status"] == "healthy"
    assert data["environment"] == "production"