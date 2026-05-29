import requests
import json

with open("config/endpoints.json") as file:
    data = json.load(file)

BASE_URL = data["base_url"]
POSTS_ENDPOINT = data["posts_endpoint"]

def test_create_post():
    payload = {
        "title": "API Testing Framework",
        "body": "Testing POST request automation",
        "userId": 1
    }

    response = requests.post(BASE_URL + POSTS_ENDPOINT, json=payload)

    assert response.status_code == 201
    assert response.json()["title"] == payload["title"]