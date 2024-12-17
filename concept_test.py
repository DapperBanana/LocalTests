
import json

def is_valid_json(json_str):
    try:
        json.loads(json_str)
        return True
    except ValueError as e:
        return False

# Test the function with some sample JSON strings
json_str1 = '{"name": "John", "age": 30, "city": "New York"}'
json_str2 = '{name: "John", age: 30, city: "New York"}'

if is_valid_json(json_str1):
    print("String 1 is a valid JSON")
else:
    print("String 1 is not a valid JSON")

if is_valid_json(json_str2):
    print("String 2 is a valid JSON")
else:
    print("String 2 is not a valid JSON")
