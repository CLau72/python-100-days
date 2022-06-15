from wsgiref import headers
from dotenv import load_dotenv
import os
import requests
from pprint import pprint
from datetime import datetime

load_dotenv()
APP_ID = os.getenv("APP_ID")
API_KEY = os.getenv("API_KEY")
SHEETY_API_KEY = os.getenv("SHEETY_API_KEY")

def exercise_input():
    exercise_query = input("What exercises did you do?: ")

    headers = {
        "x-app-id": APP_ID,
        "x-app-key": API_KEY,
        "Content-Type": "application/json"
    }

    body = {
        "query": exercise_query
    }

    response = requests.post(url="https://trackapi.nutritionix.com/v2/natural/exercise", headers=headers, json=body)
    data = response.json()
    return data

def add_workout(exercise_data={}):
    api_endpoint = "https://api.sheety.co/de3edc42051f3aa35335b4e565509b6a/workoutTracker/workouts"

    current_datetime = datetime.now()
    date = current_datetime.strftime('%d/%m/%Y')
    time = current_datetime.strftime('%X')

    headers = {
        "Authorization": SHEETY_API_KEY
    }

    for exercise in exercise_data["exercises"]:
        body = {
            "workout": {
                "date": date,
                "time": time,
                "exercise": exercise["name"].title(),
                "duration": exercise["duration_min"],
                "calories": exercise["nf_calories"]
            }
        }
        response = requests.post(url=api_endpoint, json=body, headers=headers)
        print(response.text)

def get_workouts():
    api_endpoint = "https://api.sheety.co/de3edc42051f3aa35335b4e565509b6a/workoutTracker/workouts"
    response = requests.get(url=api_endpoint, headers=headers)
    data = response.json()
    print(data)

def main():
    # exercise_input()
    add_workout(exercise_input())

    

if __name__ == "__main__":
    main()