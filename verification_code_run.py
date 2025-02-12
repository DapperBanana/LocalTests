
import json

def is_valid_json(input_string):
    try:
        json.loads(input_string)
        return True
    except json.JSONDecodeError:
        return False

input_string = input("Enter a JSON string: ")

if is_valid_json(input_string):
    print("The input string is a valid JSON.")
else:
    print("The input string is not a valid JSON.")
