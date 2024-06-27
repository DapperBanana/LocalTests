
import json

def is_valid_json(data):
    try:
        json_object = json.loads(data)
    except ValueError as e:
        return False
    return True

# Test the function
data1 = '{"name": "Alice", "age": 30, "city": "New York"}'
data2 = '{"name": "Bob", "age": 25, "city": "Chicago"}'
data3 = '{"name": "Eve", "age": 28, "city": "Los Angeles"'

print(is_valid_json(data1))  # True
print(is_valid_json(data2))  # True
print(is_valid_json(data3))  # False
