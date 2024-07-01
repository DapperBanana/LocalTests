
import json

def is_valid_json(s):
    try:
        json.loads(s)
        return True
    except ValueError:
        return False

# Test the function
json_str = '{"name": "John", "age": 30, "city": "New York"}'
if is_valid_json(json_str):
    print("The string is a valid JSON.")
else:
    print("The string is not a valid JSON.")
