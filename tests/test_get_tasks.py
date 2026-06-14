import requests

BASE_URL = "http://127.0.0.1:5000"


def test_get_tasks():

    response = requests.get(
        f"{BASE_URL}/tasks"
    )

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, list)