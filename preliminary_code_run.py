
import json

def is_valid_json(data):
    try:
        json.loads(data)
        return True
    except ValueError as e:
        return False

json_string = input("Enter a JSON string: ")

if is_valid_json(json_string):
    print("The input is a valid JSON.")
else:
    print("The input is not a valid JSON.")
