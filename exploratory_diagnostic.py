
import requests
from bs4 import BeautifulSoup

# URL of the web page containing the table
url = 'https://www.example.com/table'

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content of the web page
soup = BeautifulSoup(response.content, 'html.parser')

# Find the table on the web page
table = soup.find('table')

# Extract data from the table
data = []
rows = table.find_all('tr')
for row in rows:
    cells = row.find_all('td')
    if cells:
        data.append([cell.text.strip() for cell in cells])

# Print the extracted data
for row in data:
    print(row)
