
import json

# Read JSON file
with open('data.json') as file:
    data = json.load(file)

# Print key-value pairs
for key, value in data.items():
    print(f"{key}: {value}")
