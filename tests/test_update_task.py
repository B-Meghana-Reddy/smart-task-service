import requests

BASE_URL = "http://127.0.0.1:5000"


def test_update_task_state_verification():

    # Step 1: Create Task
    payload = {
        "title": "Update Test Task",
        "description": "Testing update",
        "priority": "Medium",
        "dueDate": "2026-06-20"
    }

    create_response = requests.post(
        f"{BASE_URL}/tasks",
        json=payload
    )

    task_id = create_response.json()["id"]

    # Step 2: Update Task
    update_payload = {
        "status": "Completed"
    }

    update_response = requests.put(
        f"{BASE_URL}/tasks/{task_id}",
        json=update_payload
    )

    assert update_response.status_code == 200

    # Step 3: Get All Tasks
    get_response = requests.get(
        f"{BASE_URL}/tasks"
    )

    tasks = get_response.json()

    # Step 4: Verify State Change
    updated_task = None

    for task in tasks:
        if task["id"] == task_id:
            updated_task = task
            break

    assert updated_task is not None
    assert updated_task["status"] == "Completed"