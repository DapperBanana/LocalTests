
import re

def is_valid_email(email):
    # Regular expression for validating an email address
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    # Use the re.match function to check if the email matches the pattern
    if re.match(email_pattern, email):
        return True
    else:
        return False

# Get the email address input from the user
email = input("Enter an email address: ")

# Check if the email address is valid
if is_valid_email(email):
    print(f"{email} is a valid email address.")
else:
    print(f"{email} is not a valid email address.")
