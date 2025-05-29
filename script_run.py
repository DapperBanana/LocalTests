
import json

# Read the JSON file
with open('data.json') as f:
    data = json.load(f)

# Print the key-value pairs
for key, value in data.items():
    print(f'{key}: {value}')
