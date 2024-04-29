
import json

def is_valid_json(json_str):
    try:
        json.loads(json_str)
    except ValueError as e:
        return False
    return True

# Test the function
json_str = '{"name": "Alice", "age": 30}'
if is_valid_json(json_str):
    print("The given string is a valid JSON.")
else:
    print("The given string is not a valid JSON.")
