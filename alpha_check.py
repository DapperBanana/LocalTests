
import json

def is_valid_json(json_str):
    try:
        json.loads(json_str)
        return True
    except ValueError as e:
        return False

# Test the function with different JSON strings
json_str1 = '{"name": "John", "age": 30, "city": "New York"}'
json_str2 = '{"name": "Jane", "age": 25, "city": "Los Angeles}'
json_str3 = '{invalid json}'

print(is_valid_json(json_str1))  # Should return True
print(is_valid_json(json_str2))  # Should return False
print(is_valid_json(json_str3))  # Should return False
