
from bs4 import BeautifulSoup
import requests

# URL of the webpage to scrape
url = 'https://www.w3schools.com/html/html_tables.asp'

# Make a GET request to fetch the webpage content
response = requests.get(url)

# Parse the webpage content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find the table we want to extract data from
table = soup.find('table', {'id': 'customers'})

# Extract data from the table
data = []
rows = table.find_all('tr')
for row in rows:
    cells = row.find_all('td')
    if len(cells) > 0:
        data.append([cell.text for cell in cells])

# Display the extracted data
for row_data in data:
    print(row_data)
