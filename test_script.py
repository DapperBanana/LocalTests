
import requests
from bs4 import BeautifulSoup

# URL of the web page
url = 'https://www.w3schools.com/html/html_tables.asp'

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Find the table in the HTML content
table = soup.find('table', attrs={'class': 'w3-table-all'})

# Extract data from the table
data = []
for row in table.find_all('tr'):
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data.append(cols)

# Print the extracted data
for row in data:
    print(row)
