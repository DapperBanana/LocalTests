
import requests
from bs4 import BeautifulSoup

url = "https://www.example.com"  # URL of the website to scrape

# Make a GET request to the website
response = requests.get(url)

# Parse the HTML content of the website
soup = BeautifulSoup(response.content, 'html.parser')

# Find specific elements on the website using BeautifulSoup
titles = soup.find_all('h2')  # Find all <h2> tags on the website

# Extract and print the text content of the titles
for title in titles:
    print(title.text)

# Find specific elements with a specific class using BeautifulSoup
items = soup.find_all(class_='item')  # Find all elements with class 'item'

# Extract and print the text content of the items
for item in items:
    print(item.text)

# Find specific elements with a specific ID using BeautifulSoup
main_div = soup.find(id='main')  # Find the element with id 'main'

# Extract and print the text content of the main div
print(main_div.text)
