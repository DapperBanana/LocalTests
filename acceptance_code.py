
import re

def is_valid_email(email):
    # Regular expression pattern for matching email address
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    
    # Check if the email matches the pattern
    if re.match(pattern, email):
        return True
    else:
        return False

# Test the function
email1 = "example@example.com"
email2 = "invalid_email.com"
email3 = "another_example@domain.com"
email4 = "test@not valid.com"

print(is_valid_email(email1))  # Output: True
print(is_valid_email(email2))  # Output: False
print(is_valid_email(email3))  # Output: True
print(is_valid_email(email4))  # Output: False
