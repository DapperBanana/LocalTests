
import json

def is_valid_json(s):
    try:
        json.loads(s)
        return True
    except json.JSONDecodeError:
        return False

# Test the function
json_string = '{"name": "John", "age": 30, "city": "New York"}'
print(is_valid_json(json_string))  # Output: True

invalid_json_string = '{"name": "John", "age": 30, "city": "New York"'
print(is_valid_json(invalid_json_string))  # Output: False
