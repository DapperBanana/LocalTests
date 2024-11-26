
import requests

def get_data_from_api(url):
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Error fetching data from API")
        return None

api_url = "https://api.example.com/data"
data = get_data_from_api(api_url)

if data:
    for item in data:
        print(item)
