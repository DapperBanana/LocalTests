
import json

def is_valid_json(input_string):
    try:
        json.loads(input_string)
        return True
    except ValueError:
        return False

# Test the function
input_string = '{"name": "John", "age": 30}'
if is_valid_json(input_string):
    print("Valid JSON")
else:
    print("Invalid JSON")
