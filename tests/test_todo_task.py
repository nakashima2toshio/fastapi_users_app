# tests/test_todo_task.py
# tests/test_todo_task.py
from fastapi import status
from sqlalchemy.orm import Session
from tests.conftest import test_client


def test_create_todo_task(test_client):
    response = test_client.post(
        "/todos",
        json={"title": "Test Task", "description": "Test Description"}
    )
    assert response.status_code == status.HTTP_201_CREATED
    data = response.json()
    assert data["title"] == "Test Task"
    assert data["description"] == "Test Description"


def test_read_todo_tasks(test_client):
    response = test_client.get("/todos")
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0


def test_update_todo_task(test_client):
    response = test_client.post(
        "/todos",
        json={"title": "Test Task", "description": "Test Description"}
    )
    assert response.status_code == status.HTTP_201_CREATED
    task_id = response.json()["id"]

    response = test_client.put(
        f"/todos/{task_id}",
        json={"title": "Updated Task", "description": "Updated Description"}
    )
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["title"] == "Updated Task"
    assert data["description"] == "Updated Description"
