
import json

def is_valid_json(json_str):
    try:
        json_object = json.loads(json_str)
    except ValueError as e:
        return False
    return True

# Test the function with sample JSON strings
json_str1 = '{"name": "John", "age": 30}'
json_str2 = '{name: "John", age: 30}'  # Invalid JSON

if is_valid_json(json_str1):
    print("The string is a valid JSON.")
else:
    print("The string is not a valid JSON.")

if is_valid_json(json_str2):
    print("The string is a valid JSON.")
else:
    print("The string is not a valid JSON.")
