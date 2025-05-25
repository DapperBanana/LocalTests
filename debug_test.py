
import json

def is_valid_json(my_str):
    try:
        json.loads(my_str)
        return True
    except ValueError:
        return False

# Example usage
my_string = '{"name": "Alice", "age": 30, "is_student": false}'
if is_valid_json(my_string):
    print("The given string is a valid JSON.")
else:
    print("The given string is not a valid JSON.")
