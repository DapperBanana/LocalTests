
import validators

def is_valid_url(url):
    return validators.url(url)

url = input("Enter a URL: ")
if is_valid_url(url):
    print("Valid URL")
else:
    print("Invalid URL")
