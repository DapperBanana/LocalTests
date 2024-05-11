
import re

def is_valid_url(url):
    # regular expression pattern for URL
    url_pattern = re.compile(
        r'^(?:http|ftp)s?://' 
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' 
        r'localhost|' 
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' 
        r'(?::\d+)?' 
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    
    return bool(url_pattern.match(url))

# test the function
url1 = "https://www.google.com"
url2 = "ftp://example.com"
url3 = "invalidURL"

print(f"Is {url1} a valid URL? {is_valid_url(url1)}")
print(f"Is {url2} a valid URL? {is_valid_url(url2)}")
print(f"Is {url3} a valid URL? {is_valid_url(url3)}")
