
from bs4 import BeautifulSoup
import requests

# Replace the URL with the URL of the web page containing the table
url = 'https://www.example.com'

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content of the web page
soup = BeautifulSoup(response.text, 'html.parser')

# Find the table element in the HTML content
table = soup.find('table')

# Extract data from the table
if table:
    rows = table.find_all('tr')
    for row in rows:
        columns = row.find_all('td')
        if columns:
            data = [col.get_text() for col in columns]
            print(data)
else:
    print('Table not found on the web page')
