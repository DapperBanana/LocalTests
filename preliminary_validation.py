
import re

def is_valid_url(url):
    pattern = r'^https?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+$'
    return re.match(pattern, url) is not None

# Example usage
url = input("Enter a URL: ")
if is_valid_url(url):
    print("Valid URL")
else:
    print("Invalid URL")
