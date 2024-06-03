# tests/test_users.py
# tests/test_user.py
from fastapi import status
from tests.conftest import test_client


def test_register_user(test_client):
    response = test_client.post(
        "/auth/register",
        json={"email": "user01@email.com", "password": "p@ss_u01", "is_active": True, "is_superuser": False,
              "is_verified": False, "username": "user01"}
    )
    assert response.status_code == status.HTTP_201_CREATED
    data = response.json()
    assert data["email"] == "user01@email.com"
    assert data["username"] == "user01"


def test_login_user(test_client):
    response = test_client.post(
        "/auth/jwt/login",
        data={"username": "user01@email.com", "password": "p@ss_u01"}
    )
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"


def test_reset_password(test_client):
    response = test_client.post(
        "/auth/reset-password",
        json={"email": "user01@email.com"}
    )
    assert response.status_code == status.HTTP_200_OK


def test_verify_user(test_client):
    response = test_client.post(
        "/auth/verify",
        json={"email": "user01@email.com"}
    )
    assert response.status_code == status.HTTP_200_OK
