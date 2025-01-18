
import requests

# Define the URL of the REST API
url = "https://jsonplaceholder.typicode.com/posts"

# Send a GET request to the API
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    
    # Print the data
    for item in data:
        print(item)
else:
    # Print an error message if the request was not successful
    print("Error: Unable to retrieve data from API")
