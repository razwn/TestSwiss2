import requests


class APIS:
    def __init__(self, api_key):
        self.api_key = api_key

    def get(self, url, params):
        headers = {
            "Authorization": self.api
        }
        response = requests.get(url, headers=headers, params=params)
        return response.json()
