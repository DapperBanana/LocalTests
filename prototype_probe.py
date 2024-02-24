
import requests

# Make a GET request to the API
response = requests.get('https://jsonplaceholder.typicode.com/posts')

# Check if the request was successful
if response.status_code == 200:
    # Convert the response to JSON format
    data = response.json()
    
    # Print the results
    for item in data:
        print(item)
else:
    print('Error: Unable to fetch data from the API')
