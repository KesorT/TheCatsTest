from pathlib import Path
from .base_api_client import BaseApiClient
import json
from configs.endpoints import ENDPOINTS, VERSIONS



class UserApiClient(BaseApiClient):
    def __init__(self):
        super().__init__()

#Categories
    def get_categories(self, **kwargs):
        return self._request("GET", f"{VERSIONS['v1']}{ENDPOINTS['categories']}", **kwargs)

#Votes
    def get_votes(self, **kwargs):
        return self._request("GET", f"{VERSIONS['v1']}{ENDPOINTS['votes']}", **kwargs)

    def get_votes_by_id(self, vote_id, **kwargs):
        return self._request("GET", f"{VERSIONS['v1']}{ENDPOINTS['votes']}/{vote_id}", **kwargs)

    def post_vote(self, data, **kwargs):
        return self._request("POST", f"{VERSIONS['v1']}{ENDPOINTS['votes']}", json=data, **kwargs)

    def delete_vote(self, vote_id):
        return self._request("DELETE", f"{VERSIONS['v1']}{ENDPOINTS['votes']}/{vote_id}")

#Favourites
    def get_favorites(self, **kwargs):
        return self._request("GET", f"{VERSIONS['v1']}{ENDPOINTS['favourites']}", **kwargs)

    def get_favourites_by_id(self, favourite_id, **kwargs):
        return self._request("GET", f"{VERSIONS['v1']}{ENDPOINTS['favourites']}/{favourite_id}", **kwargs)

    def post_favourites(self, data):
        return self._request("POST", f"{VERSIONS['v1']}{ENDPOINTS['favourites']}", json=data)

    def delete_favourites(self, favourite_id):
        return self._request("DELETE", f"{VERSIONS['v1']}{ENDPOINTS['favourites']}/{favourite_id}")

#Images

    def post_upload_image(self, data=None, files=None):
        return self._request("POST", f"{VERSIONS['v1']}{ENDPOINTS['images']}/upload", data=data, files=files)
    
    def delete_image(self, image_id):
        return self._request("DELETE", f"{VERSIONS['v1']}{ENDPOINTS['images']}/{image_id}")

#Schemas

    @staticmethod
    def load_schema(schema_name):
        schema_path = Path(__file__).parent.parent / "schemas" / schema_name
        with open(schema_path, 'r') as file:
            schema = json.load(file)
        return schema