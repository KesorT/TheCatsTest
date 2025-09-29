from jsonschema import validate
import pytest
import time

def test_get_favourites(user_client):
    get_favourites_response = user_client.get_favorites()
    assert isinstance(get_favourites_response, list), "Response must be a list"
    assert len(get_favourites_response) > 0, "Favourites list should not be empty"

def test_favourites_schema(user_client):
    time.sleep(1)  # To avoid hitting rate limits
    get_favourites_response = user_client.get_favorites()

    for favourite in get_favourites_response:
        validate(instance=favourite, schema=user_client.load_schema("get_favourites_response.json"))

def test_get_favourites_by_id(user_client, favourite_testdata):
    get_favourites_by_id_response = user_client.get_favourites_by_id(favourite_testdata["id"])
    assert get_favourites_by_id_response["id"] == favourite_testdata["id"], "Favourite ID does not match"


def test_post_favourite(user_client, image_testdata):
    favourite_data = {
        "image_id": image_testdata["id"]
    }
    post_favourite_response = user_client.post_favourites(favourite_data)
    assert post_favourite_response["image_id"] == image_testdata["id"], "Image ID does not match"

def test_delete_favourite(user_client, favourite_testdata):
    delete_favourite_response = user_client.delete_favourites(favourite_testdata["id"])


