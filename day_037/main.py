from dotenv import load_dotenv
import os
import requests
from datetime import datetime

# Constants
load_dotenv()
USERNAME = os.getenv("USERNAME")
TOKEN = os.getenv("TOKEN")

pixela_endpoint = "https://pixe.la/v1/users"

# Create User Information
def create_user():

    user_params = {
        "token": TOKEN,
        "username": USERNAME,
        "agreeTermsOfService": "yes",
        "notMinor": "yes"
    }

    #POST Request to create a user with a given token
    response = requests.post(url=pixela_endpoint, json=user_params)
    print(response.text)


# Endpoint for creating a new graph for a given user
def create_graph():
    graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

    headers = {
        "X-USER-TOKEN": TOKEN
    }

    graph_config = {
        "id": "graph1",
        "name": "Minutes Late to Work",
        "unit": "minutes",
        "type": "int",
        "color": "momiji"
    }

    # POST request to create the graph
    response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
    print(response.text)

def add_pixel():
    
    add_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1"

    headers = {
        "X-USER-TOKEN": TOKEN
    }

    pixel_config = {
        "date": "20220614",
        "quantity": "20"
    }

    response = requests.post(url=add_pixel_endpoint, json=pixel_config, headers=headers)
    print(response.text)

def update_pixel():
    
    update_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/20220614"

    headers = {
        "X-USER-TOKEN": TOKEN
    }

    pixel_config = {
        "quantity": "11"
    }

    response = requests.put(url=update_pixel_endpoint, json=pixel_config, headers=headers)
    print(response.text)

def delete_pixel():

    delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/20220614"

    headers = {
        "X-USER-TOKEN": TOKEN
    }

    response = requests.delete(url=delete_endpoint, headers=headers)

current_time = datetime.now()
current_time = current_time.strftime("%Y%m%d")
print(current_time)

