import pytest
from src import UserApiClient

@pytest.fixture(scope="session")
def user_client():
    return UserApiClient()
