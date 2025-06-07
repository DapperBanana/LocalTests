
import requests

url = 'https://jsonplaceholder.typicode.com/posts'

response = requests.get(url)

if response.status_code == 200:
    posts = response.json()
    
    for post in posts:
        print(f"Post #{post['id']}: {post['title']}")
    
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")
