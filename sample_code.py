
import requests

# Make a GET request to the REST API
response = requests.get('https://jsonplaceholder.typicode.com/posts')

# Check if the request was successful
if response.status_code == 200:
    # Convert the response to JSON
    data = response.json()

    # Print the results
    for post in data:
        print(f"Post ID: {post['id']}")
        print(f"Title: {post['title']}")
        print(f"Body: {post['body']}")
        print('-------------------------------')
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")
