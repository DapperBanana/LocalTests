
import requests

def fetch_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error:", response.status_code)
        return None

def print_results(data):
    if data:
        for item in data:
            print(item)
    else:
        print("No data to display")

# Example usage: Fetch and print data from a REST API
api_url = "https://api.example.com/data"
data = fetch_data(api_url)
print_results(data)
