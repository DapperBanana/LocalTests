
import json

def is_valid_json(my_str):
    try:
        json.loads(my_str)
        return True
    except ValueError:
        return False

# Testing the function
my_string = '{"name": "John", "age": 30, "city": "New York"}'
if is_valid_json(my_string):
    print("The string is a valid JSON")
else:
    print("The string is not a valid JSON")
