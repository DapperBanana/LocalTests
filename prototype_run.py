
from bs4 import BeautifulSoup
import requests

# URL of the web page containing the table
url = 'https://www.example.com'

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content of the web page using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Find all table tags on the web page
tables = soup.find_all('table')

# Extract data from each table
for table in tables:
    rows = table.find_all('tr')
    for row in rows:
        columns = row.find_all('td')
        for column in columns:
            print(column.text)
        print('---')

# Note: You may need to modify the code to suit the specific structure of the web page you are working with
