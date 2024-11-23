
from bs4 import BeautifulSoup
import requests

# URL of the web page with the HTML table
url = 'https://www.w3schools.com/html/html_tables.asp'

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content of the web page
soup = BeautifulSoup(response.content, 'html.parser')

# Find the HTML table on the web page
table = soup.find('table', {'id': 'customers'})

# Extract data from the table
data = []
for row in table.find_all('tr'):
    cols = row.find_all('td')
    cols = [col.text.strip() for col in cols]
    data.append(cols)

# Print the extracted data
for row in data:
    print(row)
