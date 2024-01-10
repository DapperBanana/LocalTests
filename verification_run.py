
import urllib.parse

def is_valid_url(url):
    # Parse the given URL
    parsed_url = urllib.parse.urlparse(url)

    # Check if the scheme and netloc are present
    if parsed_url.scheme and parsed_url.netloc:
        return True

    return False

# Main program
url = input("Enter a URL: ")
if is_valid_url(url):
    print("Valid URL")
else:
    print("Invalid URL")
