
import json

def is_valid_json(my_json):
    try:
        json.loads(my_json)
        return True
    except ValueError as e:
        return False

# Test the function
my_json1 = '{"name": "John", "age": 30, "city": "New York"}'
my_json2 = '{"name": "Jane", "age: 25, "city": "Los Angeles"}'
my_json3 = '{"name": "Bob", "age": 40, "city": "Chicago", "married": true}'

print(is_valid_json(my_json1))  # Output: True
print(is_valid_json(my_json2))  # Output: False
print(is_valid_json(my_json3))  # Output: True
