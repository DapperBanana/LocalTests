
import requests

url = 'https://jsonplaceholder.typicode.com/users'

response = requests.get(url)

data = response.json()

for user in data:
    print(f"Name: {user['name']}")
    print(f"Username: {user['username']}")
    print(f"Email: {user['email']}")
    print("Address:")
    print(f"Street: {user['address']['street']}")
    print(f"City: {user['address']['city']}")
    print(f"Zipcode: {user['address']['zipcode']}")
    print("---------------")
