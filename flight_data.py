class FlightData:

    def __init__(self, some_data: dict):
        self.data = some_data

    def retrieve_important_from_data(self):
        """this function retrieves prices, dates of departure and link of flights from received json"""
        self.list_of_prices = [[el["price"], el["route"][0]["local_departure"], el["deep_link"]] for el in self.data["data"]]
        return self.list_of_prices

    def find_cheapest_flight(self):
        """this function finds the nearest cheapest flight and returns the flight details such as the price, date of
         departure and the link to the servise"""
        return self.list_of_prices[0]
