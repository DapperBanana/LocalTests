
import requests

# Make a GET request to the API
response = requests.get("https://api.example.com/data")

# Check if the request was successful
if response.status_code == 200:
    # Print the data retrieved from the API
    data = response.json()
    for item in data:
        print(item)
else:
    print("Error fetching data from API. Status code:", response.status_code)
