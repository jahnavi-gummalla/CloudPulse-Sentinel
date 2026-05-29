import requests
import json
from jsonschema import validate
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from logger import logger

with open("config/endpoints.json") as file:
    data = json.load(file)

BASE_URL = data["base_url"]
USERS_ENDPOINT = data["users_endpoint"]

def test_get_user_status_code():
    logger.info("Testing user status code API")
    response = requests.get(BASE_URL + USERS_ENDPOINT)
    assert response.status_code == 200
    logger.info("Test completed successfully")



def test_get_user_response_fields():
    logger.info("Validating user response fields")
    response = requests.get(BASE_URL + USERS_ENDPOINT)
    body = response.json()

    assert "id" in body
    assert "name" in body
    assert "email" in body
    assert "address" in body
    logger.info("Test completed successfully")

def test_get_user_schema_validation():
    logger.info("Validating user schema")
    response = requests.get(BASE_URL + USERS_ENDPOINT)
    body = response.json()

    with open("schemas/user_schema.json") as file:
        schema = json.load(file)

    validate(instance=body, schema=schema)
    logger.info("Test completed successfully")

def test_response_time():
    logger.info("Checking API response time")
    response = requests.get(BASE_URL + USERS_ENDPOINT)

    assert response.elapsed.total_seconds() < 2
    logger.info("Test completed successfully")

def test_invalid_endpoint():

    logger.info("Testing invalid endpoint")

    response = requests.get(BASE_URL + "/invalidendpoint")

    assert response.status_code == 404

    logger.info("Invalid endpoint test completed successfully")