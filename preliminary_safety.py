
from bs4 import BeautifulSoup
import requests

# URL of the webpage with the table
url = 'https://www.w3schools.com/html/html_tables.asp'

# Sending a GET request to the URL
resp = requests.get(url)

# Parsing the HTML content of the webpage
soup = BeautifulSoup(resp.text, 'html.parser')

# Finding the table element in the HTML content
table = soup.find('table', {'id': 'customers'})

# Extracting data from the table
data = []
for row in table.find_all('tr'):
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data.append([ele for ele in cols if ele])

# Printing the extracted data
for row in data:
    print('\t'.join(row))
