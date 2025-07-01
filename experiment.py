
import requests
import json

url = "https://api.example.com/data"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    for item in data:
        print(item)
else:
    print("Failed to retrieve data from API. Status code:", response.status_code)
