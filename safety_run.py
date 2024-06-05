
import json

def is_valid_json(input_str):
    try:
        json.loads(input_str)
        return True
    except ValueError as e:
        return False

input_str = input("Enter a string to check if it is a valid JSON: ")
if is_valid_json(input_str):
    print("The input string is a valid JSON.")
else:
    print("The input string is not a valid JSON.")
