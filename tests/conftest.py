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
def image_id(user_client):
    endpoint = "images/search"
    response = user_client.get(endpoint=endpoint)
    image_data = response.json()
    
    if image_data:
        yield image_data[0] 
    else:
        pytest.fail("API call to 'images/search' returned no images.")

    print(f"\nCleaning up image with ID: {image_data[0]['id']}")
    user_client.delete_image(image_id=image_data[0]['id'])

@pytest.fixture()
def vote_id(user_client, image_id):
    vote_data = {
        "image_id": image_id["id"],
        "value": 1
    }
    response = user_client.post_vote(vote_data)
    vote_data = response.json()
    
    yield vote_data

    print(f"\nCleaning up vote with ID: {vote_data['id']}")
    user_client.delete_vote(vote_id=vote_data['id'])

@pytest.fixture()
def favourite_id(user_client, image_id):
    favourite_data = {
        "image_id": image_id["id"]
    }
    response = user_client.post_favourites(favourite_data)
    favourite_data = response.json()
    
    yield favourite_data

    print(f"\nCleaning up favourite with ID: {favourite_data['id']}")
    user_client.delete_favourite(favourite_id=favourite_data['id'])


