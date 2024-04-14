
import requests

url = 'https://jsonplaceholder.typicode.com/posts'
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    for post in data:
        print(f"Title: {post['title']}")
        print(f"Body: {post['body']}")
        print()
else:
    print(f"Failed to fetch data from API. Status code: {response.status_code}")
