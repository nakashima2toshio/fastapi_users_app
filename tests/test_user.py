# tests/test_users.py
from fastapi import status
from sqlalchemy.orm import Session
from tests.conftest import test_client


def test_register_user(test_client):
    response = test_client.post(
        "/auth/register",
        json={"username": "testuser", "email": "testuser@example.com", "password": "testpassword"}
    )
    assert response.status_code == status.HTTP_201_CREATED
    data = response.json()
    assert data["username"] == "testuser"
    assert data["email"] == "testuser@example.com"


def test_login_user(test_client):
    response = test_client.post(
        "/auth/jwt/login",
        data={"username": "testuser", "password": "testpassword"}
    )
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"
