
import re

def is_valid_url(url):
    regex = r'^https?://(?:www\.)?[a-zA-Z0-9-]+\.[a-z]{2,}([a-zA-Z0-9_~#%&//?=+:\.-]*$)?$'

    if re.match(regex, url):
        return True
    else:
        return False

url = input("Enter a URL: ")

if is_valid_url(url):
    print("The URL is valid.")
else:
    print("The URL is not valid.")
