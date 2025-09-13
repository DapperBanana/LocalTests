
import requests
from bs4 import BeautifulSoup

# URL of the web page containing the table
url = 'https://www.w3schools.com/html/html_tables.asp'

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content of the web page
soup = BeautifulSoup(response.text, 'html.parser')

# Find the HTML table on the web page
table = soup.find('table', {'id': 'customers'})

# Extract data from the table
data = []
rows = table.find_all('tr')

for row in rows:
    cols = row.find_all('td')
    cols = [col.text.strip() for col in cols]
    data.append(cols)

# Print the extracted data
for row in data:
    print(row)
