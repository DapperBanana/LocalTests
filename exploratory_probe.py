
import json

def is_valid_json(json_str):
    try:
        json.loads(json_str)
        return True
    except ValueError as e:
        return False

# Test the function with a JSON string
json_str = '{"name": "John", "age": 30}'
if is_valid_json(json_str):
    print("The string is a valid JSON.")
else:
    print("The string is not a valid JSON.")
