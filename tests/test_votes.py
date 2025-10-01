import os
import requests
from jsonschema import validate
import pytest


def test_get_votes(user_client, vote_testdata):
    get_votes_response = user_client.get_votes()
    assert isinstance(get_votes_response, list), "Response must be a list"
    assert len(get_votes_response) > 0, "Votes list should not be empty"

def test_votes_schema(user_client, vote_testdata):
    get_votes_response = user_client.get_votes()
    validate(instance=get_votes_response[0], schema=user_client.load_schema("get_votes_response.json"))

def test_get_votes_by_id(user_client, vote_testdata):
    get_votes_by_id_response = user_client.get_votes_by_id(vote_testdata["id"])
    assert get_votes_by_id_response["id"] == vote_testdata["id"], "Vote ID does not match"

def test_post_vote_positive(user_client, image_testdata):
    vote_data = {
        "image_id": image_testdata[0]["id"],
        "value": 1
    }
    post_vote_response = user_client.post_vote(vote_data)
    assert post_vote_response["image_id"] == image_testdata[0]["id"], "Image ID does not match"
    assert post_vote_response["value"] == 1, "Vote value does not match"


@pytest.mark.parametrize(
        "vote_value, expected_status, comment",
        [
            (0, [400], "Invalid vote value 0"),
            (6, [400], "Invalid vote value 6"),
            (-1, [400], "Invalid negative vote value"),
            (None, [400], "Invalid None vote value"),
            (-5, [400], "Invalid vote value -5"),
            ("a", [400], "Invalid non-integer vote value"),
        ]
)
def test_post_vote_negative(user_client,  image_testdata, vote_value, expected_status, comment):
    vote_data = {
        "image_id": image_testdata[0]["id"],
        "value": vote_value
    }
    post_vote_response = user_client.post_vote(vote_data, raise_for_status=False)
    assert post_vote_response.status_code in expected_status, f"Unexpected status code: {post_vote_response.status_code}"

    vote_json = post_vote_response.json()
    assert vote_json["image_id"] == image_testdata[0]["id"], "Image ID does not match"
    assert vote_json["value"] == vote_value, "Vote value does not match"

def test_delete_vote(user_client, image_testdata):
    vote_data = {
        "image_id": image_testdata[0]["id"],
        "value": 1
    }
    post_vote_response = user_client.post_vote(vote_data)
    delete_vote_response = user_client.delete_vote(post_vote_response["id"])
