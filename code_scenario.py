
from bs4 import BeautifulSoup
import requests

# URL of the web page containing the table
url = "https://www.example.com/table.html"

# Make a GET request to the URL
response = requests.get(url)

# Parse the HTML content of the web page using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find the table element in the HTML content
table = soup.find('table')

# Extract data from the table
data = []
for row in table.find_all('tr'):
    row_data = []
    for cell in row.find_all(['td', 'th']):
        row_data.append(cell.text)
    data.append(row_data)

# Print the extracted data
for row in data:
    print(row)
