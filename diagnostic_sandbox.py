
import json

# Open the JSON file
with open('data.json') as file:
    data = json.load(file)

# Print the key-value pairs
for key, value in data.items():
    print(f'{key}: {value}')
