
from urllib.parse import urlparse

def validate_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except:
        return False

# Test the function with some example URLs
urls = ["https://www.google.com", "http://www.example.com", "invalidurl", "ftp://ftp.example.com"]

for url in urls:
    if validate_url(url):
        print(f"{url} is a valid URL")
    else:
        print(f"{url} is an invalid URL")
