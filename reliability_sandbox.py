
import requests
from bs4 import BeautifulSoup

url = 'https://example.com'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Extracting all the titles from the webpage
titles = soup.find_all('h1')
for title in titles:
    print(title.text)

# Extracting all the links from the webpage
links = soup.find_all('a')
for link in links:
    print(link.get('href'))
