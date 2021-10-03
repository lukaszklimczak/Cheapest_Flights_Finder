from dotenv import find_dotenv, load_dotenv
from datetime import datetime
from dateutil.relativedelta import relativedelta
import os
from flight_search import FlightSearch
from flight_data import FlightData

load_dotenv(find_dotenv())

APIKEY = os.environ.get("API_key")

TODAY = datetime.now().strftime("%d/%m/%Y")
PERIOD = (datetime.now() + relativedelta(months=+6)).strftime("%d/%m/%Y")

IATA_FROM = "WAW"
IATA_1 = "MIL"
IATA_2 = "LIS"
IATA_3 = "LON"
IATA_4 = "BER"
IATAS = [IATA_1, IATA_2, IATA_3, IATA_4]

KIWI_URL = "https://tequila-api.kiwi.com/v2/search"

finded_flights = FlightSearch(APIKEY, TODAY, PERIOD, IATA_FROM, IATA_1, KIWI_URL)
finded_flights.make_headers()
finded_flights.make_parameters()
kiwi_data = finded_flights.make_requests()

flight_data = FlightData(kiwi_data)
flight_data.retrieve_important_from_data()
flight_data.find_cheapest_flight()

