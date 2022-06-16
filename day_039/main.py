#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from operator import index
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager
from pprint import pprint

data_manager = DataManager()
flight_search = FlightSearch()

sheet_data = data_manager.get_flight_data()


# Fill in IATA codes
for i,city in enumerate(sheet_data):
    if city["iataCode"]:
        pass
        # flight_data = FlightData(destination_iata=city["iataCode"])
        # flight_search.flight_search(flight_data.search_data)
    else:
        city["iataCode"] = flight_search.iata_search(city)
        data_manager.update_flight_data(i, city)

    flight_data = flight_search.flight_search(city["iataCode"])
    if flight_data:
        print(f"{city['city']}: ${flight_data.price}")
    else:
        print(f"No direct flights to {city['city']}")
        