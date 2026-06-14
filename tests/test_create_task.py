import requests

BASE_URL = "http://127.0.0.1:5000"


def test_create_task():

    payload = {
        "title": "Pytest Task",
        "description": "Testing Create API",
        "priority": "High",
        "dueDate": "2026-06-20"
    }

    response = requests.post(
        f"{BASE_URL}/tasks",
        json=payload
    )

    assert response.status_code == 201

    data = response.json()

    assert "id" in data
    assert data["message"] == "Task created successfully"