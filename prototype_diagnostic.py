
import requests

def get_data_from_api(url):
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Error: Unable to fetch data from API")
        return None

api_url = 'https://jsonplaceholder.typicode.com/posts'
data = get_data_from_api(api_url)

if data:
    for post in data:
        print(f"Post {post['id']}: {post['title']}")
else:
    print("No data available")
