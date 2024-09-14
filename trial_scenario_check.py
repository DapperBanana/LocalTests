
import requests
import json

def get_data_from_api(url):
    response = requests.get(url)
    data = response.json()
    return data

def process_data(data):
    for item in data:
        print(f"Name: {item['name']}")
        print(f"Age: {item['age']}")
        print(f"City: {item['city']}")
        print()

if __name__ == "__main__":
    api_url = "https://api.example.com/data"
    data = get_data_from_api(api_url)
    process_data(data)
