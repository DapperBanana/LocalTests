
import json

def is_valid_json(json_str):
    try:
        json_obj = json.loads(json_str)
    except ValueError as e:
        return False
    return True

# Test the function with some examples
json_str1 = '{"name": "John", "age": 30, "city": "New York"}'
json_str2 = '{"name": "Mary", "age": 25, "city": "Chicago"}'

print(f"Is {json_str1} a valid JSON? {is_valid_json(json_str1)}")
print(f"Is {json_str2} a valid JSON? {is_valid_json(json_str2)}")
