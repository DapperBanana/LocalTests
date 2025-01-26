
import re

def is_valid_url(url):
    # Regular expression pattern to match URLs
    url_pattern = re.compile(
        r'^(https?://)?'  # Check for http:// or https:// at the beginning
        r'([a-zA-Z0-9.-]+)'  # Check for domain name
        r'([/][\w.-]*)*'  # Check for path
        r'$'
    )

    # Check if the input string matches the URL pattern
    if re.match(url_pattern, url):
        return True
    else:
        return False

# Test the function with some example URLs
urls = ["https://www.google.com", "http://example.com/page", "invalid_url", "ftp://ftp.example.com"]

for url in urls:
    if is_valid_url(url):
        print(f"{url} is a valid URL")
    else:
        print(f"{url} is not a valid URL")
