
import requests
from bs4 import BeautifulSoup

# URL of the website to scrape
url = 'https://example.com'

# Send a GET request to the website
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Extract specific information from the website
titles = soup.find_all('h1')  # Find all h1 tags on the website

for title in titles:
    print(title.text)  # Print the text content of each h1 tag

# You can add more code here to extract additional information from the website

