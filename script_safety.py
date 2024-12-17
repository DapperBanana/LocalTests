
import json

def is_valid_json(data):
    try:
        json.loads(data)
        return True
    except ValueError:
        return False

# Test the function with some sample strings
string1 = '{"name": "John", "age": 30, "city": "New York"}'
string2 = '{name: "John", age: 30, city: "New York"}'
string3 = '{"name": "John", "age": 30, "city": "New York"'

print(is_valid_json(string1))  # Output: True
print(is_valid_json(string2))  # Output: False
print(is_valid_json(string3))  # Output: False
