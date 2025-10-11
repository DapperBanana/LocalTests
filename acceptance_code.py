
import validators

def check_url(url):
    if validators.url(url):
        print(f"{url} is a valid URL.")
    else:
        print(f"{url} is not a valid URL.")

url = input("Enter a URL: ")
check_url(url)
