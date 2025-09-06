
from bs4 import BeautifulSoup
import requests

# URL of the webpage with the HTML table
url = 'https://www.example.com'

# Sending a GET request to the webpage
response = requests.get(url)

# Checking if the response is successful
if response.status_code == 200:
    # Parsing the HTML content of the webpage
    soup = BeautifulSoup(response.content, 'html.parser')

    # Finding all tables on the webpage
    tables = soup.find_all('table')

    # Extracting data from the first table found on the webpage
    if len(tables) > 0:
        table = tables[0]
        rows = table.find_all('tr')
        
        for row in rows:
            columns = row.find_all('td')
            for column in columns:
                print(column.get_text())
    else:
        print('No tables found on the webpage')

else:
    print('Failed to retrieve webpage')

