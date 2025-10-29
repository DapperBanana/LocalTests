
import json

def is_valid_json(my_json):
    try:
        json.loads(my_json)
    except ValueError as e:
        return False
    return True

# Test the function
test_json = '{"name": "Alice", "age": 30}'
print(is_valid_json(test_json))  # Output: True

test_json2 = '{"name": "Bob", "age": 25, "city": "New York}'
print(is_valid_json(test_json2))  # Output: False
