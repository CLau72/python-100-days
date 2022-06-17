from flight_data import FlightData
from dotenv import load_dotenv
import os
from twilio.rest import Client

load_dotenv()
TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_TOKEN = os.getenv("TWILIO_TOKEN")
TWILIO_NUMBER = os.getenv("TWILIO_NUMBER")


class NotificationManager:

    def __init__(self) -> None:
        self.twilio_sid = TWILIO_SID
        self.twilio_token = TWILIO_TOKEN
        self.twilio_number = TWILIO_NUMBER
        self.receiving_number= ""

    def flight_alert(self,flight_data: FlightData):
        client = Client(self.twilio_sid, self.twilio_token)

        message_body = (f"Low price alert! Only ${flight_data.price} to fly from " 
        f"{flight_data.origin_city}-{flight_data.origin_airport} to "
       f"{flight_data.destination_city}-{flight_data.destination_airport} "
        f"from {flight_data.out_date} to {flight_data.return_date}")

        message = client.messages \
                .create(
                     body=message_body,
                     from_=self.twilio_number,
                     to=self.receiving_number
                 )

        print(message.sid)
