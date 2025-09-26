from jsonschema import validate
import pytest
import time

def test_get_favourites(user_client):
    response = user_client.get_favorites()
    assert response.status_code == 200, f"Unexpected status code: {response.status_code}"

    data = response.json()
    assert isinstance(data, list), "Response must be a list"
    assert len(data) > 0, "Favourites list should not be empty"

def test_favourites_schema(user_client):
    time.sleep(1)  # To avoid hitting rate limits
    response = user_client.get_favorites()
    assert response.status_code == 200

    data = response.json()
    for favourite in data:
        validate(instance=favourite, schema=user_client.load_schema("get_favourites_response.json"))

def test_get_favourites_by_id(user_client, favourite_id):
    response = user_client.get_favourites_by_id(favourite_id["id"])
    assert response.status_code == 200, f"Unexpected status code: {response.status_code}"

    data = response.json()
    assert data["id"] == favourite_id["id"], "Favourite ID does not match"

    user_client.delete_favourites(favourite_id=data["id"])

def test_post_favourite(user_client, image_id):
    favourite_data = {
        "image_id": image_id["id"]
    }
    response = user_client.post_favourites(favourite_data)
    assert response.status_code in [200, 201], f"Unexpected status code: {response.status_code}"

    data = response.json()
    user_client.delete_favourites(favourite_id=data["id"])

def test_delete_favourite(user_client, favourite_id):
    response = user_client.delete_favourites(favourite_id["id"])
    assert response.status_code == 200, f"Unexpected status code : {response.status_code}"

    user_client.delete_favourites(favourite_id=favourite_id["id"])

