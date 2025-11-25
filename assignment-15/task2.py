import requests
import json

def get_weather_details(city_name, api_key):
    """
    Fetches and displays weather details for a city using the OpenWeatherMap API.

    Args:
        city_name (str): The name of the city.
        api_key (str): Your OpenWeatherMap API key.
    """
    # Construct the API URL
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric'  # To get temperature in Celsius
    }
    
    # Make the API request
    response = requests.get(base_url, params=params)
    
    # Get the JSON data from the response
    weather_data = response.json()
    
    # Display the JSON output in a readable format
    print(json.dumps(weather_data, indent=4))

# --- Example Usage ---
if __name__ == "__main__":
    # Using the API key you provided.
    API_KEY = '82f64f033da200034c12f7d1af5ea963' 
    
    city = input("Enter city name: ")
    print(f"\nFetching weather for {city}...\n")
    get_weather_details(city, API_KEY)
