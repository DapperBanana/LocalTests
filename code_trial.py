
import re

def is_valid_email(email):
    # regular expression to check if the email is valid
    pattern = re.compile(r'^[\w\.-]+@[a-zA-Z\d-]+\.[a-zA-Z]{2,4}$')
    
    if pattern.match(email):
        return True
    else:
        return False

# Get the email address input from the user
email = input("Enter an email address: ")

if is_valid_email(email):
    print("Valid email address.")
else:
    print("Invalid email address.")
