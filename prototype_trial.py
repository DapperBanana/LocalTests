
import json

def is_valid_json(data):
    try:
        json.loads(data)
        return True
    except ValueError as e:
        return False

# Test the function with some sample strings
sample_json = '{"name": "Alice", "age": 30}'
print(is_valid_json(sample_json))  # Output: True

invalid_json = '{"name": "Bob", "age": 25'  # Missing closing bracket
print(is_valid_json(invalid_json))  # Output: False
