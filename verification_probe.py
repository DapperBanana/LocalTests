
import json

# Open the JSON file
with open('data.json') as f:
    data = json.load(f)

# Loop through the key-value pairs and print them
for key, value in data.items():
    print(f"{key}: {value}")
