
import re

def is_valid_url(url):
    # regular expression pattern to check if URL is valid
    pattern = re.compile(
        r'^https?://'  
        r'(([0-9A-Za-z-]+\.)+[0-9A-Za-z-]+|localhost|'
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
        r'(:\d+)?'
        r'[a-zA-Z0-9-._?\:/=%&$]*$'
    )
    
    if re.match(pattern, url):
        return True
    else:
        return False

# Test cases
url1 = "https://www.google.com"
url2 = "ftp://example.com"
url3 = "invalid-url.com"

print(is_valid_url(url1))  # Output: True
print(is_valid_url(url2))  # Output: False
print(is_valid_url(url3))  # Output: False
