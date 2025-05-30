
import requests
from bs4 import BeautifulSoup

# URL of the web page containing the HTML table
url = 'https://www.w3schools.com/html/html_tables.asp'

# Send a GET request to the web page
response = requests.get(url)

# Parse the HTML content of the web page using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find the HTML table in the web page
table = soup.find('table')

# Extract data from the HTML table
data = []
for row in table.find_all('tr'):
    row_data = []
    for cell in row.find_all(['th', 'td']):
        row_data.append(cell.text.strip())
    data.append(row_data)

# Print the extracted data
for row in data:
    print('\t'.join(row))
