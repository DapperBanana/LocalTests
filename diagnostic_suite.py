
import json

# Read the JSON file
with open('data.json') as json_file:
    data = json.load(json_file)

# Print key-value pairs
for key, value in data.items():
    print(f"{key}: {value}")
