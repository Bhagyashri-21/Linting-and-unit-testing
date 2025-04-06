import random
import string
from datetime import datetime, timedelta, timezone
from fastapi.testclient import TestClient
from app.main import app
import pytest


def generate_random_string(length=10):
    """Generate a random string of fixed length"""
    return ''.join(
        random.choice(string.ascii_letters + string.digits)
        for _ in range(length))


@pytest.fixture
def client():
    """Provides a test client for FastAPI"""
    return TestClient(app)


@pytest.fixture
def group(client):
    """Fixture to create a group for testing"""
    group_data = {"name": generate_random_string(12)}
    response = client.post("/create/groups/", json=group_data)
    return response.json()


@pytest.fixture
def todo(client, group):
    """Fixture to create a todo for testing"""
    todo_data = {
        "task": "Buy groceries",
        "description": "Milk, eggs, bread",
        "assigned_by": "Ram",
        "assigned_to": "Sita",
        "group_id": group["id"],
        "due_date":
        (datetime.now(timezone.utc) + timedelta(days=3)).isoformat(),
        "priority": 1,
    }
    response = client.post("/create/todos/", json=todo_data)
    return response.json()


def test_create_todo_with_due_date_and_priority(client, group):
    """Test creating a todo with due date and priority"""
    todo_data = {
        "task": "Complete project report",
        "description": "Write and submit the project report",
        "assigned_by": "Manager",
        "assigned_to": "Sham",
        "group_id": group["id"],
        "due_date":
        (datetime.now(timezone.utc) + timedelta(days=5)).isoformat(),
        "priority": 2,
    }

    response = client.post("/create/todos/", json=todo_data)
    assert response.status_code == 200
    assert response.json()["task"] == "Complete project report"
    assert response.json()["due_date"] is not None
    assert response.json()["priority"] == 2


def test_create_subtask(client, group, todo):
    """Test creating a subtask for an existing todo"""
    subtask_data = {
        "task": "Write introduction",
        "description": "Write the introduction section of the report",
        "assigned_by": "Manager",
        "assigned_to": "Ram",
        "parent_id": todo["id"],
        "due_date":
        (datetime.now(timezone.utc) + timedelta(days=2)).isoformat(),
        "priority": 1,
    }

    response = client.post("/create/todos/", json=subtask_data)
    assert response.status_code == 200
    assert response.json()["task"] == "Write introduction"
    assert response.json()["parent_id"] == todo["id"]


def test_update_todo_due_date_and_priority(client, group, todo):
    """Test updating the due date and priority of a todo"""
    updated_data = {
        "due_date":
        (datetime.now(timezone.utc) + timedelta(days=7)).isoformat(),
        "priority": 0,
    }

    response = client.put(f"/update/todos/{todo['id']}", json=updated_data)
    assert response.status_code == 200
    assert response.json()["due_date"] is not None
    assert response.json()["priority"] == 0


def test_delete_todo_with_subtasks(client, group):
    """Test deleting a todo that has subtasks"""
    main_task_data = {
        "task": "Complete project",
        "description": "Complete all tasks for the project",
        "assigned_by": "Manager",
        "assigned_to": "Ram",
        "group_id": group["id"]
    }
    response = client.post("/create/todos/", json=main_task_data)
    main_task = response.json()
    subtask_data = {
        "task": "Prepare slides",
        "description": "Prepare slides for the project presentation",
        "assigned_by": "Manager",
        "assigned_to": "Ram",
        "parent_id": main_task["id"],
    }
    response = client.post("/create/todos/", json=subtask_data)
    subtask = response.json()
    delete_response = client.delete(f"/delete/todos/{main_task['id']}")
    assert delete_response.status_code == 200
    assert delete_response.json() == {"message": "Todo deleted successfully"}

    main_task_check = client.get(f"/get/todos/{main_task['id']}")
    subtask_check = client.get(f"/get/todos/{subtask['id']}")

    assert main_task_check.status_code == 404
    assert subtask_check.status_code == 404
