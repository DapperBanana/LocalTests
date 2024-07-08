
import requests

url = "https://jsonplaceholder.typicode.com/posts"  # Example URL to a REST API endpoint

response = requests.get(url)

if response.status_code == 200:  # Check if the request was successful
    data = response.json()  # Parse the JSON response

    for post in data:
        print(f"Title: {post['title']}")
        print(f"Body: {post['body']}")
        print("------")
else:
    print(f"Error: {response.status_code}")
