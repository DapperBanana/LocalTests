
import requests
from bs4 import BeautifulSoup

# URL of the website to scrape
url = 'https://example.com'

# Send a GET request to the website
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find and extract specific information from the website
title = soup.find('title').text
paragraphs = soup.find_all('p')

# Print the extracted information
print('Title:', title)
print('Paragraphs:')
for i, p in enumerate(paragraphs):
    print(f'Paragraph {i+1}:', p.text)
