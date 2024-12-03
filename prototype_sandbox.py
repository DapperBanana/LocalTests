
import requests

url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url)

data = response.json()

for post in data:
    print("Post Title: ", post["title"])
    print("Post Body: ", post["body"])
    print("--------------------------")
