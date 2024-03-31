
import re

def is_valid_url(url):
    regex = r"^(https?://)?(www\d?\.)?([a-z0-9-]+)\.([a-z]{2,})(/([^\s]*))?$"
    if re.match(regex, url):
        return True
    else:
        return False

url = input("Enter a URL: ")
if is_valid_url(url):
    print("Valid URL")
else:
    print("Invalid URL")
