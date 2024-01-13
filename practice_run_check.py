
import requests
import json

# Function to fetch data from JSON API
def fetch_api_data(url):
    try:
        response = requests.get(url)
        data = json.loads(response.text)
        return data
    except requests.exceptions.RequestException as error:
        print(f"An error occurred: {error}")
        return None

# Function to process data
def process_data(data):
    if data is not None:
        # Process data here
        for entry in data:
            # Process each entry as required
            print(entry)
    else:
        print("Error: No data to process.")

# URL of the JSON API
url = "https://jsonplaceholder.typicode.com/posts"

# Fetch data from JSON API
api_data = fetch_api_data(url)

# Process the fetched data
process_data(api_data)
