
import json

def check_valid_json(input_string):
    try:
        json.loads(input_string)
        return True
    except ValueError as e:
        return False

input_string = input("Enter a string to check if it is a valid JSON: ")

if check_valid_json(input_string):
    print("The input string is a valid JSON.")
else:
    print("The input string is not a valid JSON.")
