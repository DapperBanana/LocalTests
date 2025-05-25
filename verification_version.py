
import re

def is_valid_url(url):
    # Regex pattern for URL validation
    pattern = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https:// or ftp://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' # domain...
        r'localhost|' # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or IP
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

    if re.match(pattern, url):
        return True
    else:
        return False

# Test the function
url = "https://www.google.com"
if is_valid_url(url):
    print(f"'{url}' is a valid URL.")
else:
    print(f"'{url}' is not a valid URL.")
