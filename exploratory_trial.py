
import re

def is_valid_url(url):
    pattern = re.compile(r'^(https?|ftp)://[^\s/$.?#].[^\s]*$')
    if re.match(pattern, url):
        return True
    return False

url = input("Enter a URL to check: ")

if is_valid_url(url):
    print("The URL is valid.")
else:
    print("The URL is invalid.")
