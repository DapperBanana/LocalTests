
import re

def is_valid_email(email):
    # Regular expression to validate email address
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    
    if re.match(pattern, email):
        return True
    else:
        return False

# Test the function with some example email addresses
print(is_valid_email("example@example.com")) # True
print(is_valid_email("example@.com")) # False
print(is_valid_email("example123")) # False
