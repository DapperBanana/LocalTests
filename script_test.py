
import re

def is_valid_email(email):
    regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    
    if re.match(regex, email):
        return True
    else:
        return False

email = input("Enter an email address: ")
if is_valid_email(email):
    print("Valid email address.")
else:
    print("Invalid email address.")
