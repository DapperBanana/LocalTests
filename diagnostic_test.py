
import json

def is_valid_json(my_str):
    try:
        json.loads(my_str)
        return True
    except ValueError as e:
        return False

# Test the function
input_str = input("Enter a string to check if it is valid JSON: ")
if is_valid_json(input_str):
    print("The input is a valid JSON.")
else:
    print("The input is not a valid JSON.")
