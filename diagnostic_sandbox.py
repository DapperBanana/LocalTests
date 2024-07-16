
import requests

# Make a GET request to the API
response = requests.get('https://jsonplaceholder.typicode.com/posts')

# Check if the request was successful
if response.status_code == 200:
    # Get the JSON data from the response
    data = response.json()
    
    # Loop through the data and print each post
    for post in data:
        print("Title:", post['title'])
        print("Body:", post['body'])
        print("----------------------")
else:
    # Print an error message if the request was not successful
    print("Error: Unable to fetch data from API")
