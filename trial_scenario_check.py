
import re

def is_valid_email(email):
    pattern = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
    return bool(pattern.match(email))

email = input("Enter an email address: ")
if is_valid_email(email):
    print("Valid email address.")
else:
    print("Invalid email address.")
