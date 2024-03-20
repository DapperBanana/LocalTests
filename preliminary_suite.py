
import json

def is_valid_json(json_str):
    try:
        json.loads(json_str)
        return True
    except ValueError as e:
        return False

# Test the function with some examples
json_str1 = '{"name": "John", "age": 30, "city": "New York"}'
json_str2 = 'Invalid JSON string'

print(is_valid_json(json_str1))  # Output: True
print(is_valid_json(json_str2))  # Output: False
