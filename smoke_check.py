
import requests

# URL of the REST API
url = "https://jsonplaceholder.typicode.com/posts"

# Sending GET request to the API
response = requests.get(url)

# Checking if the request was successful
if response.status_code == 200:
    # Parsing the JSON response
    data = response.json()

    # Printing the data
    for item in data:
        print(item)
else:
    # Printing an error message if the request was not successful
    print("Error: Unable to retrieve data from the API.")
