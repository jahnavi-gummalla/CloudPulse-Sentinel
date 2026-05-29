import requests
import json

with open("config/endpoints.json") as file:
    data = json.load(file)

BASE_URL = data["base_url"]

headers = {
    "Authorization": "Bearer sample_token_123",
    "Content-Type": "application/json"
}

def test_api_headers():

    response = requests.get(
        BASE_URL + "/posts/1",
        headers=headers
    )

    assert response.status_code == 200