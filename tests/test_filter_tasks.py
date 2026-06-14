import requests

BASE_URL = "http://127.0.0.1:5000"


def test_filter_tasks_by_priority():

    # Create High Priority Task
    requests.post(
        f"{BASE_URL}/tasks",
        json={
            "title": "High Priority Task",
            "priority": "High",
            "dueDate": "2026-06-20"
        }
    )

    # Create Low Priority Task
    requests.post(
        f"{BASE_URL}/tasks",
        json={
            "title": "Low Priority Task",
            "priority": "Low",
            "dueDate": "2026-06-20"
        }
    )

    response = requests.get(
        f"{BASE_URL}/tasks?priority=High"
    )

    assert response.status_code == 200

    tasks = response.json()

    assert len(tasks) > 0

    for task in tasks:
        assert task["priority"] == "High"
    