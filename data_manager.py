import requests


class DataManager:

    def __init__(self, some_url, some_token):
        self.url = some_url
        self.token = some_token
        self.make_header()

    def make_header(self):
        self.header = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": self.token
        }
        return self.header

    def get_data_from_sheet(self):
        """This method returns the list of IATA Code and current lowest price from the google sheet"""
        self.response = requests.get(url=self.url, headers=self.header)
        self.response = self.response.json()
        self.data = [[el["iataCode"], el["lowestPrice (eur)"], el["id"]] for el in self.response["arkusz1"]]
        return self.data

    def make_list_of_iatas_from_sheet(self, some_list):
        """This method creates a list of destination points based on the google sheet data"""
        self.iatas = []
        for el in some_list:
            self.iata = {"IATA Code": el[0], "id": el[2]}
            self.iatas.append(self.iata)
        return self.iatas

    def compare_data(self, list_with_data_from_sheet, some_iata, list_with_data_from_response):
        """This method returns True if the price of the cheapest flight is lower than the flight's price in sheet"""
        for i in range(len(list_with_data_from_sheet)):
            if some_iata == list_with_data_from_sheet[i][0]:
                if list_with_data_from_sheet[i][1] > list_with_data_from_response[1]:
                    self.price = list_with_data_from_response[1]
                    return True, self.price

    def make_body_for_put(self):
        self.body = {
            "arkusz1": {
                "lowestPrice (eur)": self.price
            }
        }
        return self.body

    def make_put_request(self, some_id):
        """This method makes a put request and updates the sheet with finded flight's cheapest price"""
        self.response = requests.put(url=f"{self.url}/{some_id}", headers=self.header, json=self.body)
        self.response.raise_for_status()
