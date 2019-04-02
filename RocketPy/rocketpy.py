import requests
from RocketPy import exceptions


class RocketPy:
    def __init__(self, mode):
        self.mode = mode

    def get_page(url):
        try:
            r = requests.get(url)
            if r.status_code == 200:
                return r.text
            else:
                return None
        except (requests.exceptions.Timeout, requests.exceptions.RequestException):
            raise exceptions.GetPageError

    def get_global_stats(self):
        pass
