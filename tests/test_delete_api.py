import sys
import os
import json

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.api_client import delete_request

with open("config/endpoints.json") as file:
    data = json.load(file)

BASE_URL = data["base_url"]

def test_delete_post():

    response = delete_request(BASE_URL + "/posts/1")

    assert response.status_code == 200