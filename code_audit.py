
import requests
from bs4 import BeautifulSoup

url = 'https://example.com'
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extract information from the website
    title = soup.title.text
    paragraphs = soup.find_all('p')
    
    print('Title:', title)
    
    print('\nParagraphs:')
    for p in paragraphs:
        print(p.text)
else:
    print('Failed to retrieve the webpage. Status code:', response.status_code)
