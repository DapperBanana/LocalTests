
import requests
import json

# URL of the JSON API
url = 'https://api.example.com/data'

# Make a GET request to the API
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Load the JSON data from the response
    data = json.loads(response.text)
    
    # Process the data
    for item in data['items']:
        print(item['name'])
        print(item['description'])
else:
    print('Failed to retrieve data from the API')
