
import re

def is_valid_email(email):
    pattern = re.compile(r"[^@]+@[^@]+\.[^@]+")
    return bool(pattern.match(email))

# Test the function with some example email addresses
print(is_valid_email("example@email.com"))  # True
print(is_valid_email("invalid_email.com"))  # False
print(is_valid_email("another.example@email.com"))  # True
print(is_valid_email("example@invalid@domain.com"))  # False
