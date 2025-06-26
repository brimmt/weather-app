import requests
from dotenv import load_dotenv
import os

load_dotenv()

class City:
    def __init__(self, name, lat, lon, units="metric"):
        self.name = name
        self.lat = lat
        self.lon = lon
        self.units = units
        self.get_data()

    def get_data(self):
        BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
        API_KEY = os.getenv("WEATHER_API_KEY")  # 🔐 Eventually move to .env file

        try:
            response = requests.get(
                f"{BASE_URL}?lat={self.lat}&lon={self.lon}&units={self.units}&appid={API_KEY}"
            )
            self.response_json = response.json()
            self.temp = self.response_json["main"]["temp"]
            self.temp_min = self.response_json["main"]["temp_min"]
            self.temp_max = self.response_json["main"]["temp_max"]
        except:
            self.temp = self.temp_min = self.temp_max = None
            self.response_json = {}


def get_coordinates_from_city(city_name):
    

    from dotenv import load_dotenv
    load_dotenv()
    import os
    import requests

    API_KEY = os.getenv("WEATHER_API_KEY")
    GEO_URL = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit=1&appid={API_KEY}"

    try:
        response = requests.get(GEO_URL)
        results = response.json()

        if results:
            lat = results[0]["lat"]
            lon = results[0]["lon"]
            return lat, lon
        else:
            return None, None
    except:
        return None, None 