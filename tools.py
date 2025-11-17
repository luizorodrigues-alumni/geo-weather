import os
import requests
from langchain.tools import tool

@tool("get_location_data", description="Get geolocation info for a place. Input must be: { 'text': '<location name>' }")
def get_location_data(input: dict):
    """
    Fetches geolocation data for a given location name using the GeoApiFy API.
    Args:
        input (dict): A dictionary containing the location name under the key 'text'.
    Returns:
        dict: A dictionary with parsed geolocation data including name, country, state, county, city, longitude, and latitude.
    """
    
    api_key = os.getenv("GEO_APIFY_API_KEY")
    text = input.get("text")

    # GeoApiFy URL
    geolocation_url = "https://api.geoapify.com/v1/geocode/search"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    params = {
        "apiKey": api_key,
        "text": text,
    }

    # Get Request
    response = requests.get(url=geolocation_url, headers=headers, params=params)
    data = response.json()
    
    # Parse the response
    try:
        parsed_data = {
            "name": data["features"][0]["properties"]["name"],
            "country": data["features"][0]["properties"]["country"],
            "state": data["features"][0]["properties"]["state"],
            "county": data["features"][0]["properties"]["county"],
            "city": data["features"][0]["properties"]["city"],
            "lon": data["features"][0]["properties"]["lon"],
            "lat": data["features"][0]["properties"]["lat"]
        }
    except (IndexError, KeyError):
        parsed_data = {"error": "Location not found or invalid response from API."}
        
    return parsed_data


@tool("get_weather_data", description="Get weather info for a location. Input must be: { 'lat': '<latitude>', 'lon': '<longitude>' }")
def get_weather_data(input: dict):
    """
    Fetches weather data for given latitude and longitude using the wttr.in service.
    Args:
        input (dict): A dictionary containing 'lat' and 'lon' keys for latitude and longitude.
    Returns:
        dict: A dictionary with parsed weather data including current conditions and forecast.
    """
    lat = input.get("lat")
    lon = input.get("lon")

    #wttr.in URL
    weather_url = f"https://wttr.in/{lat},{lon}?format=j1"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    # Get Request
    response = requests.get(url=weather_url, headers=headers)
    data = response.json()

    parsed_data = {
        "current_condition": data.get("current_condition", []),
        "weather": data.get("weather", [])
    }

    # Remove "hourly" data to reduce size
    for day in parsed_data["weather"]:
        if "hourly" in day:
            del day["hourly"]

    return data