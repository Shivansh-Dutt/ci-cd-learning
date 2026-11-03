import os

from dotenv import load_dotenv

from app import app

load_dotenv()

def test_health():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200

def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200

def test_login():
    client = app.test_client()
    response = client.post(
        "/login",
        json={
            "username": os.environ["TEST_USERNAME"],
            "password": os.environ["TEST_PASSWORD"]
        }
    )

    assert response.status_code == 200
    assert response.json["message"] == "Login successful"
