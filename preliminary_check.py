
import json

def is_valid_json(input_string):
    try:
        json.loads(input_string)
    except ValueError as e:
        return False
    return True

# Test the function with various input strings
input_strings = [
    '{"name": "Alice", "age": 30}',
    '{"name": "Bob", "age": 25, "city": "New York"}',
    '{"name": "Charlie", "age": 35}',
    '{"name": "David", "age": 40, "city": "Los Angeles"}',
    '{"name": "Eve", "age": 28}'
]

for string in input_strings:
    if is_valid_json(string):
        print(f'The string "{string}" is a valid JSON.')
    else:
        print(f'The string "{string}" is not a valid JSON.')
