
import re

def is_valid_email(email):
    email_regex = r'^[\w\.-]+@[a-zA-Z\d-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email)

email = input("Enter an email address: ")

if is_valid_email(email):
    print("Valid email address.")
else:
    print("Invalid email address.")
