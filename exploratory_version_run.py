
import re

def is_valid_email(email):
    # Regular expression pattern for validating email addresses
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    
    if re.match(pattern, email):
        return True
    else:
        return False

# Test the function with some example email addresses
email1 = "john.doe@example.com"
email2 = "invalid_email.com"
email3 = "myemail@domain"
email4 = "test.email@com"

print(is_valid_email(email1))  # Output: True
print(is_valid_email(email2))  # Output: False
print(is_valid_email(email3))  # Output: False
print(is_valid_email(email4))  # Output: False
