
import re

def is_valid_email(email):
    # regular expression pattern for validating email addresses
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    
    if re.match(pattern, email):
        return True
    else:
        return False

# test the function
email = input("Enter an email address: ")
if is_valid_email(email):
    print("The email address is valid.")
else:
    print("The email address is not valid.")
