import os
import sys
import pathlib
from urllib import response
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))

import pytest
from api_clients import UserApiClient
from PIL import Image
import io

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

@pytest.fixture()
def vote_id(user_client, image_id):
    vote_data = {
        "image_id": image_id["id"],
        "value": 1
    }
    response = user_client.post_vote(vote_data)
    vote_data = response.json()
    
    yield vote_data

