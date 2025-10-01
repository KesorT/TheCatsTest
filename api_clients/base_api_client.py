import requests
from configs.api_config import DEFAULT_CONFIG

class BaseApiClient:
    def __init__(self, config = DEFAULT_CONFIG):
        self.base_url = config.base_url
        self.headers = {
            "x-api-key": config.api_key,
            "Content-Type": "application/json"
        }

    # def get(self, endpoint, params=None):
    #     url = f"{self.base_url}{endpoint}"
    #     response = requests.get(url, headers=self.headers, params=params)
    #     return response

    # def post(self, endpoint, data=None, files=None):
    #     url = f"{self.base_url}{endpoint}"
    #     response = requests.post(url, headers=self.headers, json=data, files=files)
    #     return response
    
    # def delete(self, endpoint):
    #     url = f"{self.base_url}{endpoint}"
    #     response = requests.delete(url, headers=self.headers)
    #     return response


    def _request(self, method, endpoint, raise_for_status=True, **kwargs):
        url = f"{self.base_url}{endpoint}"
        response = requests.request(method, url, headers=self.headers, **kwargs)
        if raise_for_status:
            response.raise_for_status()
            if response.status_code != 204:
                return response.json()
            else: return None
        return response