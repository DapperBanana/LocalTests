
import json

def is_valid_json(json_str):
    try:
        json.loads(json_str)
        return True
    except ValueError as e:
        return False

# Test the function
json_str1 = '{"name": "Alice", "age": 30}'
json_str2 = '{"name": "Bob", "age": }'

if is_valid_json(json_str1):
    print("The first string is a valid JSON")
else:
    print("The first string is not a valid JSON")

if is_valid_json(json_str2):
    print("The second string is a valid JSON")
else:
    print("The second string is not a valid JSON")
