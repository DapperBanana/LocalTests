
import validators

def is_valid_url(url):
    return validators.url(url)

url_input = input("Enter a URL: ")
if is_valid_url(url_input):
    print("Valid URL")
else:
    print("Invalid URL")
