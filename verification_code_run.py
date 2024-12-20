
import re

def is_valid_email(email):
    # Regular expression for validating an email address
    email_regex = r'^[\w\.-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,}$'
    
    if re.match(email_regex, email):
        return True
    else:
        return False

# Get user input for email address
email_address = input("Enter an email address: ")

# Check if the email address is valid
if is_valid_email(email_address):
    print("The email address is valid.")
else:
    print("The email address is not valid.")
