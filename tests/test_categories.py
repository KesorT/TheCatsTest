import os
import requests
from jsonschema import validate


def test_get_categories(user_client):
    get_categories_response = user_client.get_categories()

    assert isinstance(get_categories_response, list), "Response must be a list"
    assert len(get_categories_response) > 0, "Categories list should not be empty"



def test_categories_schema(user_client):
    get_categories_response = user_client.get_categories()

    for category in get_categories_response:
        validate(instance=category, schema=user_client.load_schema("get_category_response.json"))
