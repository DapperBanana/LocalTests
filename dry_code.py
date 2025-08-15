
import re

def is_valid_url(url):
    pattern = re.compile(
        r'^(https?://)?'  # http:// or https://
        r'([a-z0-9]+(-[a-z0-9]+)*\.)+[a-z]{2,}$'  # domain name
        r'(:[0-9]{1,5})?'  # port number
        r'(/.*)?$'  # path
    )
    return bool(re.match(pattern, url))

url = input("Enter a URL: ")
if is_valid_url(url):
    print("Valid URL")
else:
    print("Invalid URL")
