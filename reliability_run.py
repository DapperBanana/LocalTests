
import re

def is_valid_email(email):
    # regular expression pattern for validating email addresses
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    
    # check if the email address matches the pattern
    if re.match(pattern, email):
        return True
    else:
        return False

# test the function with some example email addresses
emails = ["test@example.com", "invalid_email", "john.doe@example.co.uk", "name@gmail..com"]
for email in emails:
    if is_valid_email(email):
        print(f"{email} is a valid email address.")
    else:
        print(f"{email} is not a valid email address.")
