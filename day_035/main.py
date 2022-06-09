import requests
from twilio.rest import Client

API_KEY = ""
TWILIO_SID = ""
TWILIO_API_KEY = ""
SENDING_NUMBER = ""
RECIEVING_NUMBER = ""

def get_lat_lng() -> tuple:

    parameters = {
        "q": "Mayfield Heights,OH,US",
        "appid": API_KEY
    }

    response = requests.get(url="http://api.openweathermap.org/geo/1.0/direct", params=parameters)
    response.raise_for_status()
    data = response.json()[0]
    return (data['lat'], data['lon'])

def get_weather(coordinates: tuple) -> dict:

    parameters = {
        "lat": coordinates[0],
        "lon": coordinates[1],
        "exclude": "current,minutely,daily,alerts",
        "appid": API_KEY
    }

    response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
    response.raise_for_status()
    weather_data = response.json()
    print(response.status_code)
    return weather_data

def it_gonna_rain(weather_data: dict) -> bool:

    # Grab the weather data for next 12 hours returned from the API
    # This is done by getting the list of 48 id values, and splitting that list down to the first 12 hours
    hourly_weather = [hour["weather"][0]["id"] for hour in weather_data["hourly"]][0:12]
    # Check for rain and return a bool for whether or not it will rain in the next 12 hours
    rain_today = False
    for hour in hourly_weather:
        if 200 <= hour <= 599:
            rain_today = True
            break
    return rain_today

def send_message(rain_today: bool):

    if rain_today:
        text_message = "It's gonna rain ☔"
    else:
        text_message = "No rain today! 🌞"

    account_sid = TWILIO_SID
    auth_token = TWILIO_API_KEY
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                         body=text_message,
                         from_=SENDING_NUMBER,
                         to=RECIEVING_NUMBER
                     )

    print(message.sid)


def main():
    coordinates = get_lat_lng()
    weather_data = get_weather(coordinates)
    send_message(it_gonna_rain(weather_data))

if __name__ == "__main__":
    main()