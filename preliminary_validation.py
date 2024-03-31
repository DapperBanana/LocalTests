
from bs4 import BeautifulSoup
import requests

url = 'https://example.com'  # Replace with the URL of the web page you want to extract data from

# Send a GET request to the URL
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find all tables in the HTML
tables = soup.find_all('table')

for table in tables:
    # Extract data from each table
    rows = table.find_all('tr')
    for row in rows:
        columns = row.find_all(['td', 'th'])
        for column in columns:
            print(column.get_text().strip())

# You can further process the extracted data as needed

