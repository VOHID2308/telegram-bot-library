import requests
from config import API_TOKEN


def get_current_weather(latitude: float, longitude: float) -> float:
    params = {
        'key': API_TOKEN,
        'q': f"{latitude},{longitude}"
    }
    url = 'http://api.weatherapi.com/v1/current.json'

    response = requests.get(url, params=params)

    print(response.json())


# get_current_weather(39.672651, 66.958455)
