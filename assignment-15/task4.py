import requests

API_KEY = "82f64f033da200034c12f7d1af5ea963"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    try:
        # Prepare API request
        params = {
            "q": city,
            "appid": API_KEY,
            "units": "metric"
        }

        response = requests.get(BASE_URL, params=params)
        # Raise an exception for bad status codes (4xx or 5xx)
        response.raise_for_status()

        data = response.json()

        # The OpenWeatherMap API returns a 'cod' of "404" (as a string) for a city not found.
        # While raise_for_status() handles this, an explicit check can provide a clearer message.
        if str(data.get("cod")) == "404":
            return "Error: City not found."

        # Extract weather details
        city_name = data["name"]
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        weather = data["weather"][0]["description"]

        # Return formatted result
        return (
            f"City: {city_name}\n"
            f"Temperature: {temp}°C\n"
            f"Humidity: {humidity}%\n"
            f"Weather: {weather.capitalize()}"
        )

    except requests.exceptions.HTTPError as http_err:
        # Specifically handle HTTP errors, like 404 for invalid city
        if http_err.response.status_code == 404:
            return "Error: City not found."
        return f"HTTP error occurred: {http_err}"
    except requests.exceptions.RequestException as req_err:
        return f"An error occurred with the request: {req_err}"

if __name__ == "__main__":
    city_input = input("Enter city name: ")
    print(get_weather(city_input))
