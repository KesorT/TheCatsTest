from base_api_client import BaseApiClient


class UserApiClient(BaseApiClient):
    def __init__(self):
        super().__init__()

    def get_categories(self):
        endpoint = "categories"
        return self.get(endpoint)
    
    def get_votes(self):
        endpoint = "votes"
        return self.get(endpoint)
    
    def get_votes_by_id(self, vote_id):
        endpoint = f"votes/{vote_id}"
        return self.get(endpoint)
    
    def post_vote(self, data):
        endpoint = "votes"
        return self.post(endpoint, data)
    
    def delete_vote(self, vote_id):
        endpoint = f"votes/{vote_id}"
        return self.delete(endpoint)
    
    def get_favorites(self):
        endpoint = "favourites"
        return self.get(endpoint)
    
    def get_favourites_by_id(self, favourite_id):
        endpoint = f"favourites/{favourite_id}"
        return self.get(endpoint)
    
    def post_favourites(self, data):
        endpoint = "favourites"
        return self.post(endpoint, data)
    
    def delete_favourites(self, favourite_id):
        endpoint = f"favourites/{favourite_id}"
        return self.delete(endpoint)
    
    
