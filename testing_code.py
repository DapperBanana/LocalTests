
import requests
from bs4 import BeautifulSoup

# URL of the web page containing the table
url = 'https://www.w3schools.com/html/html_tables.asp'

# Make a GET request to fetch the raw HTML content
response = requests.get(url)
html_content = response.text

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find the table in the HTML content
table = soup.find('table')

# Extract data from the table
for row in table.find_all('tr'):
    columns = row.find_all('td')
    if len(columns) > 0:
        data = [column.text for column in columns]
        print(data)
