import requests

BASE_URL = "http://127.0.0.1:5000"


def test_missing_title():

    payload = {
        "priority": "High",
        "dueDate": "2026-06-20"
    }

    response = requests.post(
        f"{BASE_URL}/tasks",
        json=payload
    )

    assert response.status_code == 400


def test_missing_due_date():

    payload = {
        "title": "Task Without Due Date",
        "priority": "High"
    }

    response = requests.post(
        f"{BASE_URL}/tasks",
        json=payload
    )

    assert response.status_code == 400


def test_invalid_priority():

    payload = {
        "title": "Invalid Priority Task",
        "priority": "Critical",
        "dueDate": "2026-06-20"
    }

    response = requests.post(
        f"{BASE_URL}/tasks",
        json=payload
    )

    assert response.status_code == 400


def test_invalid_date_format():

    payload = {
        "title": "Invalid Date Task",
        "priority": "High",
        "dueDate": "20-06-2026"
    }

    response = requests.post(
        f"{BASE_URL}/tasks",
        json=payload
    )

    assert response.status_code == 400


def test_invalid_title_type():

    payload = {
        "title": 123,
        "priority": "High",
        "dueDate": "2026-06-20"
    }

    response = requests.post(
        f"{BASE_URL}/tasks",
        json=payload
    )

    assert response.status_code == 400