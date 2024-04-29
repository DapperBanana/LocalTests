
from urllib.parse import urlparse

def is_valid_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except:
        return False

# Test the function
url1 = "https://www.example.com"
url2 = "not a valid url"

print(is_valid_url(url1)) # Output: True
print(is_valid_url(url2)) # Output: False
