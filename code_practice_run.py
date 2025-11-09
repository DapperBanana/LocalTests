
import json

def is_valid_json(data):
    try:
        json.loads(data)
        return True
    except ValueError as e:
        return False

# Test the function
json_str = '{"name": "Alice", "age": 30}'
if is_valid_json(json_str):
    print("The JSON string is valid.")
else:
    print("The JSON string is not valid.")
