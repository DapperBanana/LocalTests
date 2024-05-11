
import requests

# Make a GET request to the URL of the REST API endpoint
response = requests.get('https://jsonplaceholder.typicode.com/posts')

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Convert the response to JSON format
    data = response.json()

    # Iterate over the data and print each post
    for post in data:
        print(f"Post ID: {post['id']}")
        print(f"Title: {post['title']}")
        print(f"Body: {post['body']}")
        print("")

else:
    print("Error fetching data from the API")
