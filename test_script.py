
import json

def is_valid_json(json_str):
    try:
        json.loads(json_str)
        return True
    except ValueError as e:
        return False

# Test the function
json_str = '{"name": "John", "age": 30, "city": "New York"}'
if is_valid_json(json_str):
    print("The given string is a valid JSON.")
else:
    print("The given string is not a valid JSON.")
