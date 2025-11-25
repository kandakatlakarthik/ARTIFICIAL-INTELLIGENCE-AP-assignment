import requests
import json

def fetch_and_display_api_data(api_url):
    """
    Connects to a given API URL, sends a GET request, and
    displays the response in a pretty JSON format.

    Args:
        api_url (str): The URL of the public API endpoint.
    """
    print(f"Attempting to connect to: {api_url}")
    try:
        # Send a GET request to the API
        response = requests.get(api_url)

        # Raise an HTTPError for bad responses (4xx or 5xx)
        response.raise_for_status()

        # Parse the JSON response
        data = response.json()

        print("\nAPI Response (Pretty JSON):")
        # Display the response in a readable (pretty) JSON format
        # The 'indent' parameter makes the JSON output human-readable
        print(json.dumps(data, indent=4))

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")  # e.g., 404 Not Found, 500 Internal Server Error
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Connection error occurred: {conn_err}") # e.g., DNS failure, refused connection
    except requests.exceptions.Timeout as timeout_err:
        print(f"Timeout error occurred: {timeout_err}") # e.g., server did not send any data in the allotted amount of time
    except requests.exceptions.RequestException as req_err:
        print(f"An unexpected error occurred: {req_err}") # e.g., any other requests-related error
    except json.JSONDecodeError as json_err:
        print(f"Error decoding JSON response: {json_err}")
        print(f"Raw response content: {response.text}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Example using JSONPlaceholder's /posts endpoint
    jsonplaceholder_posts_url = "https://jsonplaceholder.typicode.com/posts"
    fetch_and_display_api_data(jsonplaceholder_posts_url)

    # You could also try another endpoint, for example, a single post:
    # jsonplaceholder_single_post_url = "https://jsonplaceholder.typicode.com/posts/1"
    # fetch_and_display_api_data(jsonplaceholder_single_post_url)

    # Or an API that might return an error (uncomment to test error handling)
    # invalid_url = "https://jsonplaceholder.typicode.com/nonexistent-endpoint"
    # fetch_and_display_api_data(invalid_url)
