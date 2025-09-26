import os
import requests
from jsonschema import validate


def test_get_categories(user_client):
    response = user_client.get_categories()
    assert response.status_code == 200, f"Unexpected status code: {response.status_code}"

    data = response.json()
    assert isinstance(data, list), "Response must be a list"
    assert len(data) > 0, "Categories list should not be empty"



def test_categories_schema(user_client):
    response = user_client.get_categories()
    assert response.status_code == 200

    data = response.json()
    for category in data:
        validate(instance=category, schema=user_client.load_schema("get_category_response.json"))
