
import json

def check_valid_json(input_str):
    try:
        json.loads(input_str)
        print("Valid JSON")
    except ValueError as e:
        print("Invalid JSON:", e)

# Test the function with some sample strings
check_valid_json('{"name": "John", "age": 30}')
check_valid_json('{"name": "Jane", "age": 25, "city": "New York"}')
check_valid_json('{"name": "Bob", "age": 35, "city": "Chicago", "married": true}')
check_valid_json('{"name": "Alice", "age": 28, "city": "Los Angeles", "pets": ["dog", "cat"]}')
check_valid_json('invalid json string')
