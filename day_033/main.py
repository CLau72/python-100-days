import time
from datetime import datetime
import requests
import smtplib

MY_LAT = 0
MY_LNG = 0

def iss_overhead():

    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    longitude = float(data["iss_position"]["longitude"])
    latitude = float(data["iss_position"]["latitude"])

    iss_position = (longitude, latitude)

    longitude_diff = iss_position[0] - MY_LNG
    latitude_diff = iss_position[1] - MY_LAT
    
    if abs(latitude_diff) <= 5 and abs(longitude_diff) <= 5:
        return True
    else:
        return False


def is_night():

    parameters = {
        "lat": MY_LAT ,
        "lng": MY_LNG,
        "formatted": 0
    }

    response = requests.get(url=f"https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()

    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    current_time = datetime.now()
    current_hour = current_time.hour

    if current_hour >= sunset or current_hour <= sunrise:
        return True

def send_email():

    email = ""
    password=""

    with smtplib.SMTP(host="") as connection:
        connection.ehlo()
        connection.starttls()
        connection.login(
            user=email,
            password=password,
            )
        connection.sendmail(
            from_addr=email,
            to_addrs="",
            msg=f"Subject:ISS Tracker\n\nISS is currently flying above nearby Latitude:{MY_LAT} Longitude:{MY_LNG}."
        )


def main():
    while True:
        if is_night():
            print("Currently nighttime. Checking if ISS is overhead")
            if iss_overhead():
                print("ISS Overhead! Sending Email...")
                send_email()
            else:
                print("ISS not currently overhead.")
        else:
            print("Currently daytime. ISS not visible")
        time.sleep(60)
    
if __name__ == "__main__":
    main()
