# tests/test_sns.py
# tests/test_sns.py
from fastapi import status
from sqlalchemy.orm import Session
from tests.conftest import test_client


def test_create_post(test_client):
    response = test_client.post(
        "/posts",
        json={"title": "Test Post", "content": "Test Content"}
    )
    assert response.status_code == status.HTTP_201_CREATED
    data = response.json()
    assert data["title"] == "Test Post"
    assert data["content"] == "Test Content"


def test_read_posts(test_client):
    response = test_client.get("/posts")
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
