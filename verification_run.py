
from bs4 import BeautifulSoup
import requests

# URL of the webpage containing the HTML table
url = 'https://www.w3schools.com/html/html_tables.asp'

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content of the webpage using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find the HTML table on the webpage
table = soup.find('table', attrs={'id': 'customers'})

# Extract data from the HTML table
data = []
rows = table.find_all('tr')
for row in rows:
    cols = row.find_all('td')
    cols = [col.text.strip() for col in cols]
    data.append(cols)

# Display the extracted data
for row in data:
    print(row)
