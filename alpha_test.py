
import requests
from bs4 import BeautifulSoup

# Specify the URL of the website to scrape
url = 'http://example.com'

# Send a GET request to the website and store the response
response = requests.get(url)

# Parse the HTML content of the website using Beautiful Soup
soup = BeautifulSoup(response.content, 'html.parser')

# Find and extract specific information from the website
title = soup.find('title').text
paragraphs = soup.find_all('p')

# Print the extracted information
print('Title:', title)
print('Paragraphs:')
for p in paragraphs:
    print(p.text)
