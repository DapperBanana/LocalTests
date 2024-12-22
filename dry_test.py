
import requests

# Make a GET request to the API endpoint
response = requests.get('https://jsonplaceholder.typicode.com/posts')

# Check if the request was successful
if response.status_code == 200:
    # Convert the response to JSON format
    data = response.json()

    # Print the data
    for post in data:
        print(f"Post ID: {post['id']}")
        print(f"Title: {post['title']}")
        print(f"Body: {post['body']}")
        print()
else:
    print(f"Error: Unable to fetch data from the API. Status code: {response.status_code}")
