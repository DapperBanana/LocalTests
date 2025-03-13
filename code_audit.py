
import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extract information from the website
    title = soup.title.text
    first_paragraph = soup.find('p').text
    
    print('Title:', title)
    print('First paragraph:', first_paragraph)

# URL of the website to scrape
url = 'https://www.example.com'

scrape_website(url)
