
import requests
from bs4 import BeautifulSoup

# URL of the web page with the HTML table
url = 'http://example.com/table.html'

# Make a GET request to the URL
response = requests.get(url)

# Parse the HTML content of the web page
soup = BeautifulSoup(response.text, 'html.parser')

# Find all HTML tables on the web page
tables = soup.find_all('table')

# Loop through each table and extract data
for table in tables:
    rows = table.find_all('tr')
    for row in rows:
        data = row.find_all('td')
        for cell in data:
            print(cell.text)
