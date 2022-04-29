from app.api.base_request import BaseRequests
from app.api.urls import Urls
from config.config import Config


class ApiClient(BaseRequests):

    def __init__(self) -> None:
        self.token = None

    def login(self):
        """Method to execute login"""
        r = self.get(Urls.LOGIN,
                     headers={'Authorization': f'Basic {Config.LOGIN_TOKEN}'})
        self.token = r.json().get('token')
        return self.token

    def get_root_folder(self):
        """Method to get root folder"""
        r = self.get(Urls.FILES_V2,
                     params={'breadcrumbs': '1', 'offset': '0', 'limit': '1000', '_': '1622700773180'},
                     headers={'x-token': self.token})
        return r.json()

    def get_specific_folder(self):
        """Method to get specific folder"""
        r = self.get(Urls.FILES_V2,
                     params={'breadcrumbs': '1', 'offset': '0', 'limit': '1000',
                             'folder_id': '84c966d5-8dce-429d-8f92-44d5e28b1581', '_': '1622700773180'},
                     headers={'x-token': self.token})
        return r.json()

    def get_count(self):
        """Method to get count folder"""
        r = self.get(Urls.FILES_COUNT_URL,
                     params={'folder_id': '84c966d5-8dce-429d-8f92-44d5e28b1581', '_': '1622700773179'},
                     headers={'x-token': self.token})
        return r.json()

    def get_runs(self):
        """Method to get runs requests"""
        r = self.get(Urls.FILES_RUN.format('7f4c7326-0a4e-4b56-a8d0-8ce002191672'),
                     params={'_': '1622700773181'},
                     headers={'x-token': self.token})
        return r.json()

    def get_analyses(self):
        """Method to get analyses requests"""
        r = self.get(Urls.FILES_ANALYSES.format('437ef8e4-b595-4fd8-a2f5-64221831e925'),
                     params={'_': '1622700773184'},
                     headers={'x-token': self.token})
        return r.json()

    def get_artifacts(self):
        """Method to get artifacts requests"""
        r = self.get(Urls.FILES_ANALYSES.format('437ef8e4-b595-4fd8-a2f5-64221831e925'),
                     params={'_': '1622700773185'},
                     headers={'x-token': self.token})
        return r.json()
