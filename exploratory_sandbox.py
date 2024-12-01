
import requests
import json

# Make a GET request to the JSON API
response = requests.get("https://jsonplaceholder.typicode.com/posts")

# Check if the request was successful
if response.status_code == 200:
    # Load the JSON data from the response
    data = json.loads(response.text)
    
    # Process the data
    for post in data:
        print(f"Post ID: {post['id']}")
        print(f"Title: {post['title']}")
        print(f"Body: {post['body']}")
        print("")

else:
    print("Failed to retrieve data from API")
