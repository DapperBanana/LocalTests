
import requests
import json

# URL of the JSON API
url = 'https://jsonplaceholder.typicode.com/posts'

# Sending a GET request to the URL
response = requests.get(url)

# Checking if the request was successful
if response.status_code == 200:
    # Parsing the JSON data
    data = response.json()

    # Processing the data
    for post in data:
        print(f"Title: {post['title']}")
        print(f"Body: {post['body']}")
        print("")

else:
    print("Error fetching data from API")
