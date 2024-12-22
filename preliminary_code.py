
from bs4 import BeautifulSoup
import requests

# URL of the web page
url = 'https://www.w3schools.com/html/html_tables.asp'

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content of the web page
soup = BeautifulSoup(response.content, 'html.parser')

# Find the table element on the web page
table = soup.find('table', {'id': 'customers'})

# Extract data from the table
data = []
for row in table.find_all('tr'):
    row_data = []
    for cell in row.find_all('td'):
        row_data.append(cell.text)
    if row_data:
        data.append(row_data)

# Print the extracted data
for row in data:
    print(row)
