import os
import requests
from jsonschema import validate
import pytest


CATEGORY_SCHEMA = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "name": {"type": "string"}
    },
    "required": ["id", "name"]
}


def test_get_categories(user_client):
    response = user_client.get_categories()
    assert response.status_code == 200, f"Unexpected status code: {response.status_code}"

    data = response.json()
    assert isinstance(data, list), "Response must be a list"
    assert len(data) > 0, "Categories list should not be empty"

    first_category = data[0]
    assert "id" in first_category
    assert isinstance(first_category["id"], int)
    assert "name" in first_category
    assert isinstance(first_category["name"], str)


def test_get_categories_without_api_key():
    base_url = os.getenv("BASE_URL")
    response = requests.get(f"{base_url}categories")  # без headers
    assert response.status_code in [200, 401], f"Unexpected status: {response.status_code}"


def test_categories_schema(user_client):
    response = user_client.get_categories()
    assert response.status_code == 200

    data = response.json()
    for category in data:
        validate(instance=category, schema=CATEGORY_SCHEMA)
