from django.conf import settings
import urllib
import requests
import json
from .signals import *

class ExchangeRateAPI:

    def __init__(self):
        self.app_id = getattr(settings, "APP_ID", "")
        self.base_url = getattr(settings, "BASE_URL", "")
        self.MAX_ATTEMPTS = 5

        if not self.app_id:
            raise ValueError("App ID is not configured.")
        if not self.base_url:
            raise ValueError("Base URL is not configured.")

    def get_latest_exchange_rates(self, url_params=''):
        '''
        1. This method calls the api to query the latest exchange rates data from the website of the Base Url.
        2. url_params is a dictionary of the additional optional params that can be sent in the API.
            For eg: url_params = {"show_alternative": True}
        '''
        success = False
        attempts = 0
        status = None
        content = None
        url = f"{self.base_url}latest.json?app_id={self.app_id}"

        if url_params:
            url_params_string = urllib.parse.urlencode(url_params)
            url += f"&{url_params_string}"

        while attempts < self.MAX_ATTEMPTS and status != 200:
            response = requests.get(url)

            status = response.status_code
            content = json.loads(response.content)
            attempts += 1
            if status == 200 and content:
                success = True
                exchange_rates_signal(content)

        if not success and content:
            raise ValueError(content["description"])

    def get_historical_exchange_rates(self, date, url_params=''):
        '''
        1. This method calls the api to query the historical exchange rates data from the website of the Base Url.
        2. url_params is a dictionary of the additional optional params that can be sent in the API.
            For eg: url_params = {"show_alternative": True}
        '''

        success = False
        attempts = 0
        status = None
        content = None
        url = f"{self.base_url}historical/{date}.json?app_id={self.app_id}"

        if url_params:
            url_params_string = urllib.parse.urlencode(url_params)
            url += f"&{url_params_string}"

        while attempts < self.MAX_ATTEMPTS and status != 200:
            response = requests.get(url)

            status = response.status_code
            content = json.loads(response.content)
            attempts += 1
            if status == 200 and content:
                success = True
                exchange_rates_signal(content)

        if not success and content:
            raise ValueError(content["description"])

