import os

import requests
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "http://127.0.0.1:5000"

def test_health():
    response = requests.get(f"{BASE_URL}/health")
    assert response.status_code == 200

def test_home():
    response = requests.get(f"{BASE_URL}/")
    assert response.status_code == 200

def test_login():
    response = requests.post(
        f"{BASE_URL}/login",
        json={
            "username": os.environ["TEST_USERNAME"],
            "password": os.environ["TEST_PASSWORD"]
        }
    )

    assert response.status_code == 200
    assert response.json()["message"] == "Login successful"
