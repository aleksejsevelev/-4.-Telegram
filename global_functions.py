import requests
import os
from dotenv import load_dotenv


def save_photo(filepath, url, params):
    response = requests.get(url, params=params)
    response.raise_for_status()
    with open(filepath, 'wb') as file:
        file.write(response.content)


def get_nasa_apikey():
    load_dotenv('secret_data.env')
    apikey = os.getenv('NASA_TOKEN')
    return apikey
