import random
import json
import os

# Define the file name for storing results
RESULTS_FILE = "results.json"

def fetch_weather_data(city: str) -> dict:
    """
    Mocks an API call to fetch weather data for a given city.
    (This would be your function from Task 4, potentially using 'requests' library)
    """
    # Simulate different weather conditions
    temperatures = [18, 22, 15, 25, 20, 10, 30]
    humidities = [60, 55, 70, 45, 65, 80, 40]
    weathers = ["Clear sky", "Few clouds", "Overcast", "Sunny", "Rainy", "Snowy", "Thunderstorms"]

    # Randomly select mock data
    temp = random.choice(temperatures)
    humidity = random.choice(humidities)
    weather = random.choice(weathers)

    return {
        "city": city,
        "temp": temp,
        "humidity": humidity,
        "weather": weather
    }

def get_and_store_weather(city: str):
    """
    Fetches weather data for a city, prints it to console,
    and appends it to a local JSON file without overwriting previous results.
    """
    # 1. Fetch the weather data using the function from Task 4
    weather_result = fetch_weather_data(city)

    # 2. Display formatted output to the console
    print(f"--- Weather for {weather_result['city']} ---")
    print(f"Temperature: {weather_result['temp']}°C")
    print(f"Humidity: {weather_result['humidity']}%")
    print(f"Conditions: {weather_result['weather']}")
    print("-" * 30)

    # 3. Read existing results from the file
    all_results = []
    if os.path.exists(RESULTS_FILE) and os.path.getsize(RESULTS_FILE) > 0:
        try:
            with open(RESULTS_FILE, 'r', encoding='utf-8') as f:
                existing_data = json.load(f)
                # Ensure the loaded data is a list, otherwise initialize fresh
                if isinstance(existing_data, list):
                    all_results = existing_data
                else:
                    print(f"Warning: {RESULTS_FILE} contains non-list JSON. Starting fresh.")
        except json.JSONDecodeError:
            print(f"Warning: {RESULTS_FILE} is corrupted or invalid JSON. Starting fresh.")
        except Exception as e:
            print(f"An unexpected error occurred while reading {RESULTS_FILE}: {e}. Starting fresh.")

    # 4. Append the new weather result
    all_results.append(weather_result)

    # 5. Write the updated list of results back to the file
    try:
        with open(RESULTS_FILE, 'w', encoding='utf-8') as f:
            json.dump(all_results, f, indent=2, ensure_ascii=False)
        print(f"Successfully stored weather data for {city} in {RESULTS_FILE}")
    except Exception as e:
        print(f"Error writing to {RESULTS_FILE}: {e}")

# --- Example Usage ---
if __name__ == "__main__":
    # Optional: Clean up results.json for a fresh start if you want to test from scratch
    # if os.path.exists(RESULTS_FILE):
    #     os.remove(RESULTS_FILE)
    #     print(f"Removed existing {RESULTS_FILE} for a fresh start.")

    print("--- Making first request: London ---")
    get_and_store_weather("London")
    print("\n--- Making second request: New York ---")
    get_and_store_weather("New York")
    print("\n--- Making third request: Paris ---")
    get_and_store_weather("Paris")
    print("\n--- Making fourth request: Tokyo ---")
    get_and_store_weather("Tokyo")

    print(f"\n--- Contents of {RESULTS_FILE} after all requests ---")
    if os.path.exists(RESULTS_FILE):
        with open(RESULTS_FILE, 'r', encoding='utf-8') as f:
            print(f.read())
    else:
        print(f"{RESULTS_FILE} was not created.")
