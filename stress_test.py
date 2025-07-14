
from bs4 import BeautifulSoup
import requests

# URL of the web page with the table
url = 'https://www.example.com/table.html'

# Send a GET request to the web page
response = requests.get(url)

# Parse the HTML content of the web page
soup = BeautifulSoup(response.content, 'html.parser')

# Find the table in the HTML content
table = soup.find('table')

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
