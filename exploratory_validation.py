
import validators

def is_valid_url(url):
    if validators.url(url):
        return True
    else:
        return False

url = input("Enter a URL: ")
if is_valid_url(url):
    print("Valid URL")
else:
    print("Invalid URL")
