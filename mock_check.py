
import json

def is_valid_json(input_string):
    try:
        json.loads(input_string)
        return True
    except ValueError as e:
        return False

# Test the program
input_string = '{"name": "John", "age": 30}'
print(is_valid_json(input_string))  # Output: True

input_string = '{"name": "Jane", "age: 25}'
print(is_valid_json(input_string))  # Output: False
