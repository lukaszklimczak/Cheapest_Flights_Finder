from dotenv import find_dotenv, load_dotenv
from datetime import datetime
from dateutil.relativedelta import relativedelta
import os
from flight_search import FlightSearch
from flight_data import FlightData
from data_manager import DataManager
from notification_manager import NotificationManager

load_dotenv(find_dotenv())

APIKEY = os.environ.get("API_key")

SHEETY_URL = os.environ.get("Sheety_url")
SHEETY_TOKEN = os.environ.get("Sheety_token")

account_sid = os.environ.get("account_sid") #regards to twilio account
auth_token = os.environ.get("auth_token") #regards to twilio account
some_from_number = os.environ.get("from_number") #regards to twilio account
some_to_number = os.environ.get("to_number") #regards to twilio account

TODAY = datetime.now().strftime("%d/%m/%Y")
PERIOD = (datetime.now() + relativedelta(months=+6)).strftime("%d/%m/%Y")

IATA_FROM = "WAW"

manager = DataManager(SHEETY_URL, SHEETY_TOKEN)

sheet_data = manager.get_data_from_sheet()
IATAS = manager.make_list_of_iatas_from_sheet(sheet_data)

KIWI_URL = "https://tequila-api.kiwi.com/v2/search"

for i, el in enumerate(IATAS):
    finded_flights = FlightSearch(APIKEY, TODAY, PERIOD, IATA_FROM, IATAS[i]["IATA Code"], KIWI_URL)
    finded_flights.make_headers()
    finded_flights.make_parameters()
    kiwi_data = finded_flights.make_requests()

    flight_data = FlightData(kiwi_data)
    flight_data.retrieve_important_from_data()
    cheapest_flight_details = flight_data.find_cheapest_flight()

    if manager.compare_data(sheet_data, IATAS[i]["IATA Code"], cheapest_flight_details):
        manager.make_body_for_put()
        manager.make_put_request(IATAS[i]["id"])
        notification = NotificationManager(account_sid, auth_token, some_from_number, some_to_number)
        notification.create_message(cheapest_flight_details)

