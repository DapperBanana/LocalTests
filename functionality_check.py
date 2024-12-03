
import requests
from bs4 import BeautifulSoup

# URL of the website to scrape
url = 'https://example.com'

# Send a GET request to the URL
response = requests.get(url)

# Use BeautifulSoup to parse the HTML content of the website
soup = BeautifulSoup(response.content, 'html.parser')

# Find all <a> tags on the website
links = soup.find_all('a')

# Print out the text and href attribute of each link
for link in links:
    print('Text:', link.text)
    print('URL:', link.get('href'))
    print('-----------------------------------')

# Find all <p> tags on the website
paragraphs = soup.find_all('p')

# Print out the text of each paragraph
for paragraph in paragraphs:
    print('Paragraph:', paragraph.text)

