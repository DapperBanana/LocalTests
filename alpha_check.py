
import re

def is_valid_email(email):
    # Regular expression to match email pattern
    pattern = r'^[\w\.-]+@[a-zA-Z\d-]+\.[a-zA-Z]{2,}$'
    
    if re.match(pattern, email):
        return True
    else:
        return False

# Get input from user
email = input("Enter an email address: ")

# Check if the email address is valid
if is_valid_email(email):
    print("The email address is valid.")
else:
    print("The email address is not valid.")
