
import json

def is_valid_json(input_string):
    try:
        json.loads(input_string)
        return True
    except ValueError:
        return False

# Test the function with some input strings
input_string1 = '{"key": "value"}'
input_string2 = '{key: value}'
input_string3 = '["item1", "item2"]'

print(f"Is input_string1 a valid JSON? {is_valid_json(input_string1)}")
print(f"Is input_string2 a valid JSON? {is_valid_json(input_string2)}")
print(f"Is input_string3 a valid JSON? {is_valid_json(input_string3)}")
