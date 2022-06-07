import requests
from datetime import datetime

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
# 
# data = response.json()
# 
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
# 
# iss_position = (longitude, latitude)
# 
# print(iss_position)
MY_LAT = 41.6188988
MY_LNG = -81.4339191

parameters = {
    "lat": MY_LAT ,
    "lng": MY_LNG
}

response = requests.get(url=f"https://api.sunrise-sunset.org/json?lat={parameters['lat']}&lng={parameters['lng']}&formatted=0")
response.raise_for_status()

data = response.json()
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]

current_time = datetime.now()
