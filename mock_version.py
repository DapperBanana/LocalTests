
import validators

def check_url(input_url):
    if validators.url(input_url):
        print("Valid URL")
    else:
        print("Invalid URL")

input_url = input("Enter a URL: ")
check_url(input_url)
