
import requests
from bs4 import BeautifulSoup

# URL of the website to scrape
url = "https://example.com"

# Send a GET request to the website
response = requests.get(url)

# Parse the HTML content of the website
soup = BeautifulSoup(response.text, "html.parser")

# Find all <a> tags to extract links
links = soup.find_all("a")
for link in links:
    print(link.get('href'))

# Find all <p> tags to extract paragraph content
paragraphs = soup.find_all("p")
for paragraph in paragraphs:
    print(paragraph.text)

# Find specific elements by class or id
specific_element_class = soup.find("div", class_="specific-class")
specific_element_id = soup.find("div", id="specific-id")
if specific_element_class:
    print(specific_element_class.text)
if specific_element_id:
    print(specific_element_id.text)
