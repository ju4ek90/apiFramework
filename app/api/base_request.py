import urllib

from config.config import Config
import requests


class BaseRequests:
    """Class for calling HTTP requests"""

    def __init__(self) -> None:
        self.token = None
        self.headers = None

    def set_token(self, token):
        self.token = token
        self.headers = {'x-token': token}

    def form_url(self, url):
        """Method to concat base url and api path"""
        return urllib.parse.urljoin(Config.BASE_URL, url)

    def get(self, path, headers={}, *args, **kwargs):
        """Reimplementation of GET method"""
        url = self.form_url(path)
        headers = {**self.headers, **headers}
        return requests.get(url=url, headers=headers, *args, **kwargs)

    def post(self, path, *args, **kwargs):
        """Reimplementation of POST method"""
        url = self.form_url(path)
        return requests.post(url, *args, **kwargs)
