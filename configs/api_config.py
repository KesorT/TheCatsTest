from dotenv import load_dotenv
import os
import pathlib
import sys
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))

load_dotenv()

class ApiConfig:
    def __init__(self, base_url: str, api_key: str):
        self.base_url = base_url
        self.api_key = api_key

DEFAULT_CONFIG = ApiConfig(
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("API_KEY")
)
