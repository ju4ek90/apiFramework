import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    """Class defines all the configuration for test framework"""

    BASE_URL = 'https://app.cosmosid.com'
    LOGIN_TOKEN = os.getenv('AUTH_KEY', None)
    TIMEOUT_LOGIN = 3
