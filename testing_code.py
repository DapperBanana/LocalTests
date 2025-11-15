
import re

def is_valid_url(url):
    # Regular expression pattern for checking a valid URL
    pattern = re.compile(r'^((http|https)://)?[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(.[a-zA-Z]{2,})?$')
    
    if pattern.match(url):
        return True
    else:
        return False

# Test the function
url1 = "https://www.google.com"
url2 = "http://www.facebook.com"
url3 = "invalid_url"

print(is_valid_url(url1))  # True
print(is_valid_url(url2))  # True
print(is_valid_url(url3))  # False
