from twilio.rest import Client

class NotificationManager:
    def __init__(self, some_account_sid, some_token, some_from_number, some_to_number):
        self.account_sid = some_account_sid
        self.token = some_token
        self.from_number = some_from_number
        self.to_number = some_to_number

    def create_message(self, some_flight_details: list):
        client = Client(self.account_sid, self.token)
        message = client.messages \
                .create(
                    body=f"The nearest cheapest flight to {some_flight_details[0]} costs EUR{some_flight_details[1]}"
                         f", starts {some_flight_details[2]}, for details click on the link: {some_flight_details[3]}",
                    from_=self.from_number,
                    to=self.to_number
        )
