from pathlib import Path
from .base_api_client import BaseApiClient
import json



class UserApiClient(BaseApiClient):
    def __init__(self):
        super().__init__()

#Categories
    def get_categories(self, **kwargs):
        return self._request("GET", "categories", **kwargs)

#Votes
    def get_votes(self, **kwargs):
        return self._request("GET", "votes", **kwargs)

    def get_votes_by_id(self, vote_id, **kwargs):
        return self._request("GET", f"votes/{vote_id}", **kwargs)

    def post_vote(self, data):
        return self._request("POST", "votes", json=data)
    
    def delete_vote(self, vote_id):
        return self._request("DELETE", f"votes/{vote_id}")

#Favourites
    def get_favorites(self, **kwargs):
        return self._request("GET", "favourites", **kwargs)

    def get_favourites_by_id(self, favourite_id, **kwargs):
        return self._request("GET", f"favourites/{favourite_id}", **kwargs)

    def post_favourites(self, data):
        return self._request("POST", "favourites", json=data)

    def delete_favourites(self, favourite_id):
        return self._request("DELETE", f"favourites/{favourite_id}")

#Images

    def post_upload_image(self, data=None, files=None):
        return self._request("POST", "images/upload", data=data, files=files)
    
    def delete_image(self, image_id):
        return self._request("DELETE", f"images/{image_id}")

#Schemas

    def load_schema(self, schema_name):
        schema_path = Path(__file__).parent.parent / "schemas" / schema_name
        with open(schema_path, 'r') as file:
            schema = json.load(file)
        return schema