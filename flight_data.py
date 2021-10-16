class FlightData:

    def __init__(self, some_data: dict):
        self.data = some_data

    def retrieve_important_from_data(self):
        """this method retrieves prices, dates of departure and link of flights from received json"""
        self.list_of_finded_flights = [[el["cityTo"], el["price"], el["route"][0]["local_departure"],
                                        el["deep_link"]] for el in self.data["data"]]
        return self.list_of_finded_flights

    def find_cheapest_flight(self):
        """this method finds the nearest cheapest flight and returns the flight details such as the destination city,
        the price, date of departure and the link to the service"""
        self.list_of_finded_flights_sorted = sorted(self.list_of_finded_flights, key=lambda x: x[1])
        return self.list_of_finded_flights_sorted[0]
