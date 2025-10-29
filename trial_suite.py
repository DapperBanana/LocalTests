
import requests
from bs4 import BeautifulSoup

# URL of the website to scrape
url = 'http://example.com'

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content of the page
soup = BeautifulSoup(response.content, 'html.parser')

# Extract specific information from the webpage
# For example, extracting all the text from <p> tags
paragraphs = soup.find_all('p')
for p in paragraphs:
    print(p.get_text())

# Extracting all the links on the page
links = soup.find_all('a')
for link in links:
    print(link.get('href'))
