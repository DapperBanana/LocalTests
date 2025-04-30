
import re

def is_valid_url(url):
    # Regular expression pattern for matching URLs
    pattern = re.compile(r"^(http|https)://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(\/\S*)?$")
    
    # Check if the URL matches the pattern
    if re.match(pattern, url):
        return True
    else:
        return False

# Test the function with some examples
print(is_valid_url("https://www.google.com")) # True
print(is_valid_url("http://example.com"))     # True
print(is_valid_url("ftp://example.com"))      # False
print(is_valid_url("www.example.com"))        # False
