import requests

BASE_URL = "http://127.0.0.1:5000"


def test_delete_task_state_verification():

    # Step 1: Create Task
    payload = {
        "title": "Delete Test Task",
        "description": "Testing delete",
        "priority": "Low",
        "dueDate": "2026-06-20"
    }

    create_response = requests.post(
        f"{BASE_URL}/tasks",
        json=payload
    )

    assert create_response.status_code == 201

    task_id = create_response.json()["id"]

    # Step 2: Delete Task
    delete_response = requests.delete(
        f"{BASE_URL}/tasks/{task_id}"
    )

    assert delete_response.status_code == 200

    # Step 3: Get All Tasks
    get_response = requests.get(
        f"{BASE_URL}/tasks"
    )

    assert get_response.status_code == 200

    tasks = get_response.json()

    # Step 4: Verify Task No Longer Exists
    task_exists = False

    for task in tasks:
        if task["id"] == task_id:
            task_exists = True
            break

    assert task_exists is False