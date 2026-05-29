import requests
import json

with open("config/endpoints.json") as file:
    data = json.load(file)

BASE_URL = data["base_url"]

def test_update_post():
    payload = {
        "id": 1,
        "title": "Updated API Testing Framework",
        "body": "Testing PUT request automation",
        "userId": 1
    }

    response = requests.put(BASE_URL + "/posts/1", json=payload)

    assert response.status_code == 200
    assert response.json()["title"] == payload["title"]