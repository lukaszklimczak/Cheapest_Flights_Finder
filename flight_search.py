import requests


class FlightSearch:

    def __init__(self, some_apikey: str, some_date_from: str, some_date_to: str, some_IATA_from: str, some_IATA_to: str,
                 some_api_url: str):
        self.apikey = some_apikey
        self.date_from = some_date_from
        self.date_to = some_date_to
        self.fly_from = some_IATA_from
        self.fly_to = some_IATA_to
        self.url = some_api_url

    def make_headers(self):
        self.headers = {
            "apikey": self.apikey,
            "Content-Encoding": "gzip"
        }
        return self.headers

    def make_parameters(self):
        self.parameters = {
            "fly_from": self.fly_from,
            "fly_to": self.fly_to,
            "date_from": self.date_from,
            "date_to": self.date_to
        }
        return self.parameters

    def make_requests(self):
        """This function makes a request to KIWI.com API """
        response = requests.get(url=self.url, headers=self.headers, params=self.parameters)
        response.raise_for_status()
        kiwi_data = response.json()
        return kiwi_data



