
from urllib.parse import urlparse

def is_valid_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except:
        return False

# Test the program
url1 = "https://www.google.com"
url2 = "www.google.com"
url3 = "http:/www.google.com"

print(is_valid_url(url1))  # Output: True
print(is_valid_url(url2))  # Output: False
print(is_valid_url(url3))  # Output: False
