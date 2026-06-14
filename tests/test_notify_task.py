import requests

BASE_URL = "http://127.0.0.1:5000"


def test_notify_existing_task():

    # Create Task
    payload = {
        "title": "Notify Test Task",
        "description": "Testing notify endpoint",
        "priority": "High",
        "dueDate": "2026-06-20"
    }

    create_response = requests.post(
        f"{BASE_URL}/tasks",
        json=payload
    )

    task_id = create_response.json()["id"]

    # Notify
    notify_response = requests.post(
        f"{BASE_URL}/tasks/{task_id}/notify"
    )

    assert notify_response.status_code == 200

    data = notify_response.json()

    assert "payload" in data
    assert data["message"] == "Notification payload validated successfully"


def test_notify_non_existing_task():

    notify_response = requests.post(
        f"{BASE_URL}/tasks/99999/notify"
    )

    assert notify_response.status_code == 404