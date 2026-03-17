from dotenv import load_dotenv
import requests
import os
import json

load_dotenv()

API_KEY = os.getenv('WEATHER_API')

def get_request(date: str, time_hour: int, lat: float, long: float): 
    '''
    GET request for weather data from visualcrossing.com

    Args: 
        date: specific date (yyyy-mm-dd)
        time_hour: hour on the 24 hour scale
        lat: latitude of area
        long: longitude of area

    Returns: Json object of the weather data
    '''

    url = f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{lat},{long}/{date}T{time_hour}:00:00?key={API_KEY}'
    
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print("Request successful!")
        return data

    else:
        print(f"Request failed with status code: {response.status_code}")


