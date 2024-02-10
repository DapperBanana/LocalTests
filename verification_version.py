
import requests
from bs4 import BeautifulSoup

# URL of the website you want to scrape
url = 'https://example.com'

# Send a GET request to the website
response = requests.get(url)

# Parse the HTML content of the website using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Extract information from the website
title = soup.title.text # Get the title of the website
links = soup.find_all('a') # Find all <a> tags (hyperlinks) on the website

# Print the extracted information
print('Website Title:', title)
print('Links:')
for link in links:
    print(link.get('href'))
