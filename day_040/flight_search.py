from dotenv import load_dotenv
from pprint import pprint
import os
import requests
from datetime import datetime, timedelta
from flight_data import FlightData


load_dotenv()
TEQUILLA_API_ENDPOINT = os.getenv("TEQUILLA_API_ENDPOINT")
TEQUILLA_API_KEY = os.getenv("TEQUILLA_API_KEY")

class FlightSearch:

    def __init__(self) -> None:
        self.api_endpoint = TEQUILLA_API_ENDPOINT
        self.api_key = TEQUILLA_API_KEY


    def iata_search(self, city_data):

        request_url = f"{TEQUILLA_API_ENDPOINT}locations/query"

        headers = {
            "apikey": self.api_key,
            "accept": "application/json"
        }

        parameters = {
            "term": city_data["city"],
            "locale": "en-US",
            "location_types": "city"
        }

        response = requests.get(url=request_url, headers=headers, params=parameters)
        data = response.json()
        return data["locations"][0]["code"]

    def flight_search(self, dest_city_code, max_stopovers=0):
        request_url = f"{TEQUILLA_API_ENDPOINT}v2/search"

        start_datetime = (datetime.now() + timedelta(days=1))
        end_datetime = (datetime.now() + timedelta(days=(6 * 30)))
        search_data = {
            "fly_from": "LON",
            "fly_to": dest_city_code,
            "date_from": start_datetime.strftime("%d/%m/%Y"),
            "date_to": end_datetime.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "cur": "USD",
            "max_stopovers": 0,
            "limit": 1
        }


        headers = {
            "apikey": self.api_key,
            "accept": "application/json"
        }

        response = requests.get(url=request_url, headers=headers, params=search_data)
        data = response.json()

        try:
            flight_data = FlightData(
                price=data["data"][0]["fare"]["adults"],
                origin_city=data["data"][0]["cityFrom"],
                destination_city=data["data"][0]["cityTo"],
                origin_airport=data["data"][0]["route"][0]["flyFrom"],
                destination_airport=data["data"][0]["route"][0]["flyTo"],
                out_date=data["data"][0]["route"][0]["local_departure"].split("T")[0],
                return_date=data["data"][0]["route"][1]["local_departure"].split("T")[0]
            )
        except IndexError:
            search_data["max_stopovers"] = 1
            response = requests.get(url=request_url, headers=headers, params=search_data)
            pprint(response.json())
        else:
            return flight_data