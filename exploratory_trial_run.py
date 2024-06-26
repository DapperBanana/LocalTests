
import re

def is_valid_url(url):
    # Regular expression pattern to match a valid URL
    pattern = re.compile(r'^(http|https)://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}/?')
    
    if pattern.match(url):
        return True
    else:
        return False

# Test the function with some example URLs
urls = ["https://www.google.com", "http://www.example.com", "invalidurl", "https://123.com"]

for url in urls:
    if is_valid_url(url):
        print(f"{url} is a valid URL")
    else:
        print(f"{url} is not a valid URL")
