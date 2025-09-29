import os
import sys
import pathlib
from urllib import response
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))

import pytest
from api_clients import UserApiClient


@pytest.fixture(scope="session")
def user_client():
    return UserApiClient()

@pytest.fixture()
def image_testdata(user_client):
    get_image_response = user_client._request("GET", "images/search")

    yield get_image_response[0]

@pytest.fixture()
def vote_testdata(user_client, image_testdata):
    vote_data = {
        "image_id": image_testdata["id"],
        "value": 1
    }
    post_vote_response = user_client.post_vote(vote_data)

    yield post_vote_response

    print(f"\nCleaning up vote with ID: {post_vote_response['id']}")
    user_client.delete_vote(vote_id=post_vote_response['id'])

@pytest.fixture()
def favourite_testdata(user_client, image_testdata):
    favourite_data = {
        "image_id": image_testdata["id"]
    }
    print(f"\nPosting favourite with data: {favourite_data}")
    post_favourite_response = user_client.post_favourites(data=favourite_data)

    yield post_favourite_response

    print(f"\nCleaning up favourite with ID: {post_favourite_response['id']}")
    user_client.delete_favourites(favourite_id=post_favourite_response['id'])


