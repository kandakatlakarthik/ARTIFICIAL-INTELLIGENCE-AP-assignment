import json

# 1. The raw JSON data from the API, stored as a string.
api_response_string = """
{
  "coord": { "lon": -0.1257, "lat": 51.5085 },
  "weather": [
    { "id": 800, "main": "Clear", "description": "clear sky", "icon": "01d" }
  ],
  "main": { "temp": 18, "feels_like": 17.9, "humidity": 60 },
  "name": "London",
  "cod": 200
}
"""

# 2. Parse the JSON string into a Python dictionary.
# If you were using the `requests` library to fetch data, you would use `response.json()`
# which does this step for you.
weather_data = json.loads(api_response_string)

# 3. Extract the specific fields by navigating the dictionary structure.
# Note that 'weather' is a list, so we access its first element with [0].
city = weather_data.get("name")
temperature = weather_data.get("main", {}).get("temp")
humidity = weather_data.get("main", {}).get("humidity")
# Capitalize the first letter of the description for better display.
description = weather_data.get("weather", [{}])[0].get("description", "").capitalize()

# 4. Display the data in a user-friendly format using an f-string.
print("--- Weather Report ---")
print(f"City: {city}")
print(f"Temperature: {temperature}°C")
print(f"Humidity: {humidity}%")
print(f"Weather: {description}")
