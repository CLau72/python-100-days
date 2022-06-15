from dotenv import load_dotenv
import os
import requests
from pprint import pprint

load_dotenv()
APP_ID = os.getenv("APP_ID")
API_KEY = os.getenv("API_KEY")

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
    pprint(data)

def main():
    exercise_input()

if __name__ == "__main__":
    main()