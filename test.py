
import re

def is_valid_email(email):
    pattern = r'^[\w\.-]+@[a-zA-Z\d\.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, email):
        return True
    else:
        return False

email = input("Enter an email address: ")
if is_valid_email(email):
    print("Valid email address")
else:
    print("Invalid email address")
