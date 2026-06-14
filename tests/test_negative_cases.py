import requests

BASE_URL = "http://127.0.0.1:5000"

def test_invalid_status():

    create_response = requests.post(
        f"{BASE_URL}/tasks",
        json={
            "title": "Status Test",
            "priority": "High",
            "dueDate": "2026-06-20"
        }
    )

    task_id = create_response.json()["id"]

    response = requests.put(
        f"{BASE_URL}/tasks/{task_id}",
        json={
            "status": "Done"
        }
    )

    assert response.status_code == 400

    

def test_update_non_existing_task():

    response = requests.put(
        f"{BASE_URL}/tasks/99999",
        json={
            "status": "Completed"
        }
    )

    assert response.status_code == 404


def test_delete_non_existing_task():

    response = requests.delete(
        f"{BASE_URL}/tasks/99999"
    )

    assert response.status_code == 404


def test_notify_non_existing_task():

    response = requests.post(
        f"{BASE_URL}/tasks/99999/notify"
    )

    assert response.status_code == 404


def test_empty_payload():

    response = requests.post(
        f"{BASE_URL}/tasks",
        json={}
    )

    assert response.status_code == 400


def test_empty_title():

    response = requests.post(
        f"{BASE_URL}/tasks",
        json={
            "title": "",
            "priority": "High",
            "dueDate": "2026-06-20"
        }
    )

    assert response.status_code == 400


def test_null_title():

    response = requests.post(
        f"{BASE_URL}/tasks",
        json={
            "title": None,
            "priority": "High",
            "dueDate": "2026-06-20"
        }
    )

    assert response.status_code == 400


def test_invalid_status():

    create_response = requests.post(
        f"{BASE_URL}/tasks",
        json={
            "title": "Status Test",
            "priority": "High",
            "dueDate": "2026-06-20"
        }
    )

    task_id = create_response.json()["id"]

    response = requests.put(
        f"{BASE_URL}/tasks/{task_id}",
        json={
            "status": "Done"
        }
    )

    assert response.status_code == 400


def test_invalid_priority_update():

    create_response = requests.post(
        f"{BASE_URL}/tasks",
        json={
            "title": "Priority Update Test",
            "priority": "High",
            "dueDate": "2026-06-20"
        }
    )

    task_id = create_response.json()["id"]

    response = requests.put(
        f"{BASE_URL}/tasks/{task_id}",
        json={
            "priority": "Critical"
        }
    )

    assert response.status_code == 400


def test_invalid_date_update():

    create_response = requests.post(
        f"{BASE_URL}/tasks",
        json={
            "title": "Date Update Test",
            "priority": "High",
            "dueDate": "2026-06-20"
        }
    )

    task_id = create_response.json()["id"]

    response = requests.put(
        f"{BASE_URL}/tasks/{task_id}",
        json={
            "dueDate": "20-06-2026"
        }
    )

    assert response.status_code == 400


def test_invalid_title_type_update():

    create_response = requests.post(
        f"{BASE_URL}/tasks",
        json={
            "title": "Type Test",
            "priority": "High",
            "dueDate": "2026-06-20"
        }
    )

    task_id = create_response.json()["id"]

    response = requests.put(
        f"{BASE_URL}/tasks/{task_id}",
        json={
            "title": 123
        }
    )

    assert response.status_code == 400