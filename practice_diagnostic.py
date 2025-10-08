
import requests

api_url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(api_url)

if response.status_code == 200:
    data = response.json()
    for post in data:
        print("Post ID:", post["id"])
        print("Title:", post["title"])
        print("Body:", post["body"])
        print()
else:
    print("Failed to fetch data from API. Status code:", response.status_code)
