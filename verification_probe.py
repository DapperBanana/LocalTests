
import requests

# Make a GET request to the REST API
response = requests.get('https://api.example.com/data')

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()

    # Print the results
    for item in data:
        print(item)
else:
    print('Error:', response.status_code)
