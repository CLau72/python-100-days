from dotenv import load_dotenv
from pprint import pprint
import os
import requests

load_dotenv()
SHEETY_API_ENDPOINT = os.getenv("SHEETY_API_ENDPOINT")
SHEETY_API_KEY = os.getenv("SHEETY_API_KEY")

class DataManager:

    def __init__(self) -> None:
        self.api_endpoint = SHEETY_API_ENDPOINT
        self.api_key = SHEETY_API_KEY

    def get_flight_data(self):

        headers = {
            "Authorization": SHEETY_API_KEY
        }
        response = requests.get(url=self.api_endpoint, headers=headers)
        data = response.json()
        return data["prices"]


    def update_flight_data(self, row, data):

        headers = {
            "Authorization": SHEETY_API_KEY
        }

        body = {
            "price": data
        }

        response = requests.put(url=f"{self.api_endpoint}/{row + 2}", headers=headers, json=body)



