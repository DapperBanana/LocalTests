
import re

def is_valid_url(url):
    pattern = re.compile(
        r'^(?:http|ftp)s?://' 
        r'(?:(?:[A-Z0-9][A-Z0-9-]{0,61}[A-Z0-9]\.)+[A-Z]{2,6}|' 
        r'localhost|' 
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' 
        r'(?::\d+)?' 
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return bool(pattern.match(url))

url = 'https://www.example.com'
if is_valid_url(url):
    print(f"{url} is a valid URL.")
else:
    print(f"{url} is not a valid URL.")
