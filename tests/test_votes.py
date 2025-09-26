import os
import requests
from jsonschema import validate
import pytest

VOTES_SCHEMA_GET = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "image_id": {"type": "string"},
        "sub_id": {"type": ["string", "null"]},
        "created_at": {"type": "string", "format": "date-time"},
        "value": {"type": "integer"},
        "country_code": {"type": ["string", "null"]},
        "image": {
            "type": "object",
            "properties": {
                "id": {"type": "string"},
                "url": {"type": "string", "format": "uri"},
                "width": {"type": "integer"},
                "height": {"type": "integer"}
            },
            "required": ["id", "url", "width", "height"]
        }
    },
    "required": ["id", "image_id", "created_at", "value", "image"]
}

def test_get_votes(user_client, vote_id):
    response = user_client.get_votes()
    assert response.status_code == 200, f"Unexpected status code: {response.status_code}"

    data = response.json()
    assert isinstance(data, list), "Response must be a list"
    assert len(data) > 0, "Votes list should not be empty"

    user_client.delete_vote(vote_id=vote_id["id"])

def test_votes_schema(user_client):
    response = user_client.get_votes()
    assert response.status_code == 200

    data = response.json()
    for vote in data:
        validate(instance=vote, schema=VOTES_SCHEMA_GET)

def test_get_votes_without_api_key():
    base_url = os.getenv("BASE_URL")
    response = requests.get(f"{base_url}/votes")
    assert response.status_code == 401, f"Unexpected status code: {response.status_code}"

def test_get_votes_by_id(user_client, vote_id):
    response = user_client.get_votes_by_id(vote_id["id"])
    assert response.status_code == 200, f"Unexpected status code: {response.status_code}"

    data = response.json()
    assert data["id"] == vote_id["id"], "Vote ID does not match"

    user_client.delete_vote(vote_id=data["id"])


def test_post_vote(user_client, image_id):
    vote_data = {
        "image_id": image_id["id"],
        "value": 1
    }
    response = user_client.post_vote(vote_data)
    assert response.status_code in [200, 201], f"Unexpected status code: {response.status_code}"

    data = response.json()
    assert data["image_id"] == image_id["id"], "Image ID does not match"
    assert data["value"] == 1, "Vote value does not match"

    user_client.delete_vote(vote_id=data["id"])

def test_delete_vote(user_client, vote_id):
    response = user_client.delete_vote(vote_id["id"])
    assert response.status_code == 200, f"Unexpected status code : {response.status_code}"

    user_client.delete_vote(vote_id=vote_id["id"])