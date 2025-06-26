from typing import Optional
from fastapi import FastAPI, Query
from pydantic import BaseModel
from weather_logic import City
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 👈 allows all origins (ok for dev)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class WeatherResponse(BaseModel):
    city: str
    temperature: float
    temp_min: float
    temp_max: float
    description: str
    unit: str

@app.get("/")
def read_root():
    return {"message": "Weather API is running!"}

@app.get("/weather", response_model=WeatherResponse)
def get_weather(
    city_name: Optional[str] = Query(None, description="City name (e.g., 'Atlanta')"),
    lat: Optional[float] = Query(None, description="Latitude (if no city name)"),
    lon: Optional[float] = Query(None, description="Longitude (if no city name)"),
    units: str = Query("imperial", description="Units: metric, imperial, or standard")
):
    if city_name:
        # 🔍 Call geocoding API to get lat/lon from city
        from weather_logic import get_coordinates_from_city
        lat, lon = get_coordinates_from_city(city_name)
        if not lat or not lon:
            return {"error": f"Could not find coordinates for {city_name}"}

    if lat is None or lon is None:
        return {"error": "You must provide either a city name or both lat and lon."}

    city = City(name=city_name or "Unknown", lat=lat, lon=lon, units=units)

    return WeatherResponse(
        city=city.response_json.get("name", city.name),
        temperature=city.temp,
        temp_min=city.temp_min,
        temp_max=city.temp_max,
        description=city.response_json["weather"][0]["description"],
        unit=units
    )


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
