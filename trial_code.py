
import requests
from bs4 import BeautifulSoup

url = 'https://examplewebsite.com'
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extract specific information from the website
    title = soup.title.text
    paragraphs = soup.find_all('p')
    
    print('Title: ', title)
    print('Paragraphs:')
    for paragraph in paragraphs:
        print(paragraph.text)
    
else:
    print('Failed to retrieve website content.')
