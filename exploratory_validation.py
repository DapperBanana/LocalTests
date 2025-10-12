
import requests
from bs4 import BeautifulSoup

# URL of the website to scrape
url = 'http://example.com'

# Send a GET request to the website
response = requests.get(url)

# Parse the HTML content of the website using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all <a> tags (links) on the website
links = soup.find_all('a')

# Print out the text content and href attribute of each link
for link in links:
    print('Text:', link.text)
    print('URL:', link.get('href'))
    print('----------------------')

# Find all <h1> tags (headings) on the website
headings = soup.find_all('h1')

# Print out the text content of each heading
for heading in headings:
    print('Heading:', heading.text)

# Find all <p> tags (paragraphs) on the website
paragraphs = soup.find_all('p')

# Print out the text content of each paragraph
for paragraph in paragraphs:
    print('Paragraph:', paragraph.text)
