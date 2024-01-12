
import json

# Function to print key-value pairs recursively
def print_json(json_obj, prefix=""):
    if isinstance(json_obj, dict):
        for key, value in json_obj.items():
            if isinstance(value, (list, dict)):
                print_json(value, prefix + key + ".")
            else:
                print(prefix + key + ": " + str(value))
    elif isinstance(json_obj, list):
        for item in json_obj:
            print_json(item, prefix)

# Read JSON file
file_name = input("Enter the JSON file name: ")
with open(file_name, 'r') as file:
    json_data = json.load(file)

# Print key-value pairs
print("Key-Value Pairs:")
print_json(json_data)
