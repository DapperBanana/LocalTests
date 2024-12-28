
from bs4 import BeautifulSoup
import requests

# URL of the web page containing the table
url = 'https://www.w3schools.com/html/html_tables.asp'

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content of the web page
soup = BeautifulSoup(response.text, 'html.parser')

# Find the table element on the page (you may need to inspect the page's HTML to find the correct table element)
table = soup.find('table')

# Extract data from the table
data = []
for row in table.find_all('tr'):
    data_row = []
    for cell in row.find_all('td'):
        data_row.append(cell.text)
    data.append(data_row)

# Print the extracted data
for row in data:
    print(row)
