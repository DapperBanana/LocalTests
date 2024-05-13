
import requests

# URL of the REST API
url = 'https://jsonplaceholder.typicode.com/posts'

# Make a GET request to the API
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Get the JSON data from the response
    data = response.json()
    
    # Print each post from the API
    for post in data:
        print(f"Title: {post['title']}")
        print(f"Body: {post['body']}")
        print("------------")
else:
    print(f"Error: {response.status_code}")
