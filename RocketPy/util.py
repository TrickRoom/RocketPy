from .exceptions import GetPageError
import requests

class Util:

    @staticmethod
    def get_page(url):
        try:
            request = requests.get(url)
            return request
        except (requests.exceptions.Timeout, requests.exceptions.RequestException):
            raise GetPageError

